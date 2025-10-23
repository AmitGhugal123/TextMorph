<h1 align="center"> 🧬 TextMorph – Advanced Text Summarization & Paraphrasing</h1>


<p align="center">
<b> TextMorph </b> is an AI-powered NLP application that intelligently <b>summarizes</b> and <b>paraphrases</b> long or complex text.  
It integrates Hugging Face Transformer models and GROQ APIs into a seamless Streamlit interface to deliver real-time, high-quality text generation.
</p>



<p align="center">
  <img src="https://img.shields.io/badge/Made%20With-💖_Python_3.10+-blueviolet?style=flat-square" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-ff4b4b?style=flat-square&logo=streamlit" />
  <img src="https://img.shields.io/badge/NLP-HuggingFace-FCC624?style=flat-square&logo=huggingface" />
  <img src="https://img.shields.io/badge/AI-GROQ_API-8A2BE2?style=flat-square&logo=ai" />
  <img src="https://img.shields.io/badge/License-MIT-success?style=flat-square" />
</p>

<h6 align="center">
  <b>AI-Powered NLP App for Summarizing and Paraphrasing Texts in Real-Time</b><br>
  <i>Built with Streamlit • Hugging Face • GROQ API</i>
</p>
</h6>

## 🚀 Features

- 🔹 **Abstractive & Extractive Summarization** – Generate context-aware or concise summaries.  
- 🔹 **AI-Based Paraphrasing** – Rephrase sentences intelligently while preserving meaning.  
- 🔹 **Streamlit User Interface** – Clean, responsive, and interactive web-based UI.  
- 🔹 **Environment-Driven Configuration** – Securely manage API keys using `.env`.  
- 🔹 **Configurable Pipelines** – Modular structure for easy model extension.  
- 🔹 **YAML & Logging Integration** – Centralized configuration and debug support.

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | Streamlit |
| **Backend** | Python |
| **AI/NLP** | Hugging Face Transformers, GROQ API |
| **Configuration** | dotenv |
| **Logging** | Python logging module |
| **Environment** | Virtualenv |

---

## 🤖 AI Models
| Model | Developer | Purpose |
|--------|------------|----------|
| **BART (`facebook/bart-large-cnn`)** | Meta (Facebook AI) | Text Summarization |
| **LLaMA 3.1 (`llama-3.1-8b-instant`)** | Meta AI | Text Paraphrasing |

---

## 📂 File Structure
<pre>

summarize-paraphrase-mvp/
│
├── 📂 config/                 # Configuration files
│   ├── config.yml             # Main YAML configuration
│   ├── config_loader.py       # Python loader to read config.yml
│   └── test_config.py         # Test script for config
│
├── 📂 logs/                   # Log files
│   └── log_20251023.log
│
├── 📂 mvp/                    # Core application modules
│   ├── __init__.py
│   ├── abstractive.py         # Abstractive summarization
│   ├── extractive.py          # Extractive summarization
│   ├── logger.py              # Logging utilities
│   ├── mvp_pipeline.py        # Main processing pipeline
│   ├── paraphraser.py         # Paraphrasing module
│   ├── test_logger.py         # Test logging
│   └── test_run.py            # Test running pipeline
│
├── 📂 dist/                   # Distribution / build folder
│
├── .env                       # Environment variables for API keys
├── .gitignore                 # Git ignore file
├── app.py                     # Main app script
├── ui_app.py                  # UI / Streamlit app
├── pyproject.toml             # Project configuration for Python
├── requirements.txt           # Dependencies
└── README.md                  # Project README



</pre>

---

## ⚙️ Installation

Follow these steps to set up and run **TextMorph** locally:

```bash
# 1️⃣ Clone this repository
git clone https://github.com/<your-username>/TextMorph.git
cd TextMorph

# 2️⃣ Create a virtual environment
python -m venv venv
venv\Scripts\activate     # On Windows
# or
source venv/bin/activate  # On macOS/Linux

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Set your API keys
Create a `.env` file in the root directory:
HF_API_KEY="your_huggingface_api_key"
GROQ_API_KEY="your_groq_api_key"

# 5️⃣ Run the Streamlit app
streamlit run app.py
💡 Usage
Launch the app using the above command.

Paste your text into the input field.

Choose a processing mode: Abstractive, Extractive, or Paraphrasing.

Click Run to generate AI-based results instantly.

```

## 🧠 Model Pipeline Example

```bash
from mvp.mvp_pipeline import SummarizationPipeline

pipeline = SummarizationPipeline()
summary = pipeline.summarize_text("Your long article here...")
paraphrase = pipeline.paraphrase_text("Sentence to reword...")
```
---

🌟 Acknowledgements
- 🔹Hugging Face Transformers

- 🔹Streamlit

- 🔹GROQ API

- 🔹Python dotenv

🧩 “Simplify. Transform. Morph your text with intelligence.”

---
### 📌 Upload Steps to GitHub
1. Save this file as **`README.md`** in your project’s root folder.  
2. In VS Code terminal:  
   ```bash
   git add README.md
   git commit -m "Added professional README"
   git push origin main

---

## 👨‍💻 Developer

Amit R Ghugal <br>


📧 amitghugal1512@gmail.com


---
## 🪪 License
This project is licensed under the MIT License.

---