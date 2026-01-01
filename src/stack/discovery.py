from pathlib import Path


def find_config_files(directory="."):
    """
    Scans a directory for common config extensions.
    """
    valid_extensions = {".json", ".yaml", ".yml", ".toml", ".env"}
    found_files = []

    path = Path(directory)
    search_dirs = [path, path / "config"]

    for d in search_dirs:
        if d.exists() and d.is_dir():
            for file in d.iterdir():
                if file.suffix in valid_extensions:
                    found_files.append(file)
    return found_files
