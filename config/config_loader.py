# config/config_loader.py

import yaml
import os

class ConfigLoader:
    def __init__(self, config_path=None):
        """
        Initialize ConfigLoader.
        If no path is given, it defaults to config/config.yml
        """
        self.config_path = config_path or os.path.join(os.path.dirname(__file__), 'config.yml')
        self.config = self.load_config()

    def load_config(self):
        """Load YAML file and replace environment variable placeholders"""
        with open(self.config_path, 'r') as f:
            cfg = yaml.safe_load(f)
        return self._replace_env_vars(cfg)

    def _replace_env_vars(self, cfg):
        """Recursively replace ${VAR} with os.environ values"""
        if isinstance(cfg, dict):
            return {k: self._replace_env_vars(v) for k, v in cfg.items()}
        elif isinstance(cfg, list):
            return [self._replace_env_vars(i) for i in cfg]
        elif isinstance(cfg, str) and cfg.startswith("${") and cfg.endswith("}"):
            env_var = cfg[2:-1]
            return os.environ.get(env_var, None)
        else:
            return cfg

    def get(self, key, default=None):
        """Access nested keys using dot notation, e.g., 'models.summarization.model_name'"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            value = value.get(k, default)
            if value == default:
                break
        return value


# Optional: test loader
if __name__ == "__main__":
    cfg = ConfigLoader()
    print("HuggingFace Key:", cfg.get("api.huggingface_api_key"))
    print("Summarization Model:", cfg.get("models.summarization.model_name"))
    print("Streamlit Port:", cfg.get("app.streamlit_port"))
