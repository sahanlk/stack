def deep_merge(base, override):
    """
    Recursively merges 'override' into 'base'.
    """
    for key, value in override.items():
        if key in base and isinstance(base[key], dict) and isinstance(value, dict):
            deep_merge(base[key], value)
        else:
            base[key] = value
    return base


def unflatten_env(env_vars, prefix="STACK__"):
    """
    Turns {'STACK__DB__PORT': '5432'} into {'DB': {'PORT': 5432}}
    """
    nested_dict = {}

    for key, value in env_vars.items():
        if key.startswith(prefix):
            parts = key[len(prefix) :].split("__")

            current = nested_dict
            for part in parts[:-1]:
                if part not in current:
                    current[part] = {}
                current = current[part]

            last_key = parts[-1]
            current[last_key] = parse_value(value)

    return nested_dict


def parse_value(val):
    if val.lower() == "true":
        return True
    if val.lower() == "false":
        return False
    try:
        return int(val)
    except ValueError:
        return val


if __name__ == "__main__":
    defaults = {"app": {"debug": False, "port": 8080}, "db": {"host": "localhost"}}

    user_settings = {"app": {"debug": True}, "db": {"host": "prod-db"}}

    result = deep_merge(defaults, user_settings)
    print(result)
