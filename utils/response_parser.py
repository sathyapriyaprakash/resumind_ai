import json
import re

def clean_json_response(raw_text: str) -> dict:
    text = re.sub(r'```json\s*', '', raw_text)
    text = re.sub(r'```\s*', '', text)
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse Gemini JSON: {e}\nResponse was: {raw_text}")