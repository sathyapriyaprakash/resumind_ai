# Simplified regex-based basic parser for immediate UI needs before AI analysis
import re

def extract_basic_details(text: str) -> dict:
    emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
    phones = re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)
    return {
        "email": emails[0] if emails else "Not Found",
        "phone": phones[0] if phones else "Not Found"
    }