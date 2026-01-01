import os

from .core import deep_merge, unflatten_env
from .discovery import find_config_files
from .parsers import parse_file, parse_env
from .utils import ConfigBox


def load(directory=".", prefix="STACK__"):
    final_dict = {}

    files = find_config_files(directory)
    for file_path in files:
        if file_path.suffix == ".env":
            env_content = file_path.read_text()
            flat_env = parse_env(env_content)
            file_data = unflatten_env(flat_env, prefix="")
        else:
            file_data = parse_file(file_path)

        final_dict = deep_merge(final_dict, file_data)

    system_env = unflatten_env(dict(os.environ), prefix=prefix)
    final_dict = deep_merge(final_dict, system_env)
    return ConfigBox(final_dict)
