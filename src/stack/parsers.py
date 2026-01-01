import json


def parse_file(file_path):
    suffix = file_path.suffix
    content = file_path.read_text()

    if suffix == ".json":
        return json.loads(content)

    if suffix in [".yaml", ".yml"]:
        try:
            import yaml

            return yaml.safe_load(content)
        except ImportError:
            print("Warning: .yaml found but PyYAML not installed.")
            return {}
    return {}


def parse_env(content):
    """
    Turns a string of KEY=VALUE into a flat dictionary.
    """
    env_dict = {}
    for line in content.splitlines():
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        if "=" in line:
            key, value = line.split("=", 1)
            env_dict[key.strip()] = value.strip().strip('"').strip("'")
    return env_dict
