import pdfplumber

def extract_text_from_pdf(pdf_path: str) -> str:
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted: 
                    text += extracted + "\n"
    except Exception as e:
        raise Exception(f"Failed to read PDF: {str(e)}")
    
    if not text.strip():
        raise ValueError("PDF appears to be empty or unreadable.")
    
    return text