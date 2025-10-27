1. Set up the virtual environment
2. Install dependencies
3. Run your Streamlit app



### 🧭 **Project Setup Guide**

#### **1. Clone or Download the Project**

```bash
git clone <repository-url>
cd TextMorph
```

#### **2. Create and Activate Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate
```


#### **3. Install Dependencies**

Make sure you have `pip` updated:

```bash
pip install --upgrade pip
```

Then install all required packages:

```bash
pip install -r requirements.txt
```

---

#### **4. Run the Application**

Your main app file appears to be `ui_app.py`, which looks like a Streamlit interface.

Run it using:

```bash
streamlit run ui_app.py
```

---

#### **5. Optional: Running the Backend Script**

If `app.py` handles backend logic (like model serving), you can run it separately:

```bash
python app.py
```

---

#### **6. Folder Overview**

| Folder/File        | Description                                        |
| ------------------ | -------------------------------------------------- |
| `config/`          | Configuration files (API keys, constants, etc.)    |
| `logs/`            | Logging output                                     |
| `mvp/`             | Core logic of the summarization/paraphrasing model |
| `ui_app.py`        | Streamlit frontend application                     |
| `requirements.txt` | List of dependencies                               |
| `.env`             | Environment variables (API keys, etc.)             |

---

#### **7. Deactivating the Environment**

When done:

```bash
deactivate
```
