# Ensures the repository root is importable (so `import src.app...` resolves)
# and the app runs in deterministic stub mode during tests.
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
os.environ.setdefault("USE_STUB_MODEL", "1")
os.environ.setdefault("USAGE_LOG_PATH", "reports/usage/usage-test.jsonl")
