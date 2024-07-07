import tomllib
from typing import Dict, Any, List

def load_config() -> Dict[str, Any]:
    with open("config.toml", "rb") as config_file:
        return tomllib.load(config_file)
