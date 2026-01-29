import pdfplumber
import docx

def read_txt(uploaded_file):
    return uploaded_file.read().decode("utf-8", errors="ignore")

def read_pdf(uploaded_file):
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def read_docx(uploaded_file):
    document = docx.Document(uploaded_file)
    return "\n".join([para.text for para in document.paragraphs])
