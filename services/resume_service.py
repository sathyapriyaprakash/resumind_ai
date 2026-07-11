from utils.extractor import extract_text_from_pdf
from services.gemini_service import get_gemini_analysis

def process_resume(pdf_path: str, jd: str = "") -> dict:
    text = extract_text_from_pdf(pdf_path)
    analysis = get_gemini_analysis(text, jd)
    return text, analysis