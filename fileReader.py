import PyPDF2
import docx

def extractText(filePath):
    # Text & code files
    if filePath.endswith((".txt", ".py", ".java", ".js", ".c", ".cpp")):
        with open(filePath, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()

    # PDF files
    elif filePath.endswith(".pdf"):
        text = ""
        with open(filePath, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                if page.extract_text():
                    text += page.extract_text()
        return text

    # DOCX files
    elif filePath.endswith(".docx"):
        document = docx.Document(filePath)
        return " ".join(p.text for p in document.paragraphs)

    return ""
