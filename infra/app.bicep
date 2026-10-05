// infra/app.bicep — reuse-first deploy for the baseline buildout.
// Creates ONLY the new Container App (stock-guru-fresh) in the EXISTING rg-stock-guru:
// it references the already-provisioned Container Apps environment, ACR, Azure OpenAI
// (gpt-4.1-mini) and the app managed identity (which already holds OpenAI User + AcrPull),
// so no shared infra is re-provisioned and no new role assignments are needed. No keys.

@description('Location.')
param location string = resourceGroup().location

@description('New Container App name for this buildout.')
param appName string = 'stock-guru-fresh'

@description('Base name of the original project whose shared infra is reused.')
param baseName string = 'stock-guru'

@description('Model deployment name (existing Azure OpenAI deployment).')
param modelName string = 'gpt-4.1-mini'

@description('Container image (CI passes the real ACR image; placeholder for first apply).')
param image string = 'mcr.microsoft.com/k8se/quickstart:latest'

var suffix = uniqueString(resourceGroup().id)
var acrName = 'acr${suffix}'
var aoaiName = 'aoai-${baseName}-${suffix}'

resource appUami 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' existing = {
  name: 'id-${baseName}-app'
}

resource acr 'Microsoft.ContainerRegistry/registries@2023-11-01-preview' existing = {
  name: acrName
}

resource aoai 'Microsoft.CognitiveServices/accounts@2024-10-01' existing = {
  name: aoaiName
}

resource env 'Microsoft.App/managedEnvironments@2024-03-01' existing = {
  name: 'cae-${baseName}'
}

resource app 'Microsoft.App/containerApps@2024-03-01' = {
  name: appName
  location: location
  identity: {
    type: 'UserAssigned'
    userAssignedIdentities: { '${appUami.id}': {} }
  }
  properties: {
    managedEnvironmentId: env.id
    configuration: {
      ingress: { external: true, targetPort: 8000, transport: 'auto' }
      registries: [
        { server: acr.properties.loginServer, identity: appUami.id }
      ]
    }
    template: {
      containers: [
        {
          name: appName
          image: image
          resources: { cpu: json('0.5'), memory: '1Gi' }
          env: [
            { name: 'AOAI_ENDPOINT', value: aoai.properties.endpoint }
            { name: 'AOAI_DEPLOYMENT', value: modelName }
            { name: 'AZURE_CLIENT_ID', value: appUami.properties.clientId }
          ]
        }
      ]
      scale: { minReplicas: 0, maxReplicas: 2 }
    }
  }
}

output acrName string = acr.name
output acrLoginServer string = acr.properties.loginServer
output aoaiEndpoint string = aoai.properties.endpoint
output appFqdn string = app.properties.configuration.ingress.fqdn
output appResourceName string = app.name
