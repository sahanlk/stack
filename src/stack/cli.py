import json
import sys

from . import load


def main():
    try:
        config = load()
        print("--- Stack Configuration ---")
        print(json.dumps(config._data, indent=2))
    except Exception as e:
        print(f"Error loading stack: {e}")
        sys.exit(1)
