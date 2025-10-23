# test_config.py

from config_loader import ConfigLoader

cfg = ConfigLoader()

print("Project Name:", cfg.get("project.name"))
print("Summarization Model:", cfg.get("models.summarization.model_name"))
print("HuggingFace API Key:", cfg.get("api.huggingface_api_key"))
print("Groq API Key:", cfg.get("api.groq_api_key"))           # Added Groq key
print("Groq Endpoint:", cfg.get("api.groq_endpoint"))         # Optional: endpoint
print("Logging File:", cfg.get("logging.file"))
