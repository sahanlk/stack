
class ConfigBox:
    def __init__(self, data):
        self._data = data

    def __getattr__(self, name):
        if name in self._data:
            value = self._data[name]
            if isinstance(value, dict):
                return ConfigBox(value)
            return value
        raise AttributeError(f"'ConfigBox' object has no attribute '{name}'")

    def __repr__(self):
        return f"ConfigBox({self._data})"


