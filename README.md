## A lightweight, layered configuration engine for Python.

stack takes the pain out of managing application settings. It automatically discovers your configuration files, merges them with environment variables, and lets you access everything with clean dot-notation.

### Why use stack?
Auto-Discovery: No more manual file loading. stack finds your .json, .yaml, .toml, and .env files automatically.
 
`The Priority Stack:` Environment variables always beat files, and files beat defaults. Change behavior without changing code.

`Zero Boilerplate`: Access nested settings like config.db.host instead of config["db"]["host"].

`Type Smart`: Automatically converts "true" to True and "8080" to 8080.

`Lightweight`: Zero mandatory dependencies.

### Installation


`pip install python-stack-config`

Optional: If you use YAML files, install the yaml extra:

`pip install "python-stack-config[yaml]"`


### Quick Start
1. Create a config file
Place a file named settings.json in your project root:

**JSON**

```
{
  "server": {
    "port": 8080,
    "debug": false
  }
}
```

2. Set an environment variable (Optional)
Override settings from your terminal:

`export STACK__SERVER__PORT=9000`

3. Load it in Python


```
import stack

config = stack.load()

print(config.server.port)  # Output: 9000 (Env Var wins!)
print(config.server.debug) # Output: False (From JSON)
```

### How the "Stack" Works
stack builds your configuration in layers. Each layer overwrites the one below it:

`Project Files:` Scans for .json, .yaml, .toml in your root or /config folder.

`Local Secrets:` Loads .env files.

`System Environment:` Loads variables prefixed with STACK__.


### Advanced Usage
#### Custom Prefix
Don't like STACK__? Use your own:

```python
import stack

config = stack.load(prefix="MYAPP__")
```
Dot-Notation Access
stack recursively wraps your data, so even deeply nested keys work perfectly:

`config.database.auth.password`

### Contributing
We love community contributions! To add support for a new file format or a new cloud provider plugin:

1. Fork the repo.
2. Create your feature branch.
3. Submit a Pull Request.

### License
Distributed under the MIT License. See LICENSE for more information.
