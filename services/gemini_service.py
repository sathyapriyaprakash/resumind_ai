import google.generativeai as genai
from config import GEMINI_API_KEY, MODEL_NAME
from utils.response_parser import clean_json_response

def get_gemini_analysis(text: str, jd: str = "") -> dict:
    if not GEMINI_API_KEY:
        raise ValueError("Missing GEMINI_API_KEY in environment.")
    
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(MODEL_NAME)
    
    prompt = f"""
    You are an expert ATS and Senior Recruiter. Analyze this resume. 
    Target Job Description (if any): {jd}
    
    Resume Text:
    {text}
    
    Return STRICT JSON exactly matching this structure:
    {{
      "resume_score": 95,
      "ats_score": 91,
      "resume_health": "Excellent",
      "summary": ["Point 1", "Point 2"],
      "strengths": ["Strength 1"],
      "weaknesses": ["Weakness 1"],
      "skills_found": ["Python", "AWS"],
      "missing_skills": ["Docker"],
      "career_recommendations": [{{"role": "Role Name", "match": 95, "reason": "Reason"}}],
      "learning_plan": [{{"duration": "2 weeks", "goal": "Learn X"}}],
      "recommended_projects": ["Project Idea 1"]
    }}
    """
    
    response = model.generate_content(prompt)
    return clean_json_response(response.text)

def get_chat_response(history, user_msg, context):
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(MODEL_NAME)
    
    system_prompt = f"You are Resumind AI. Context of the resume: {context}"
    chat = model.start_chat(history=[{"role": "user", "parts": [system_prompt]}, {"role": "model", "parts": ["Understood."]}])
    
    for msg in history:
        chat.history.append({"role": msg["role"], "parts": [msg["content"]]})
        
    response = chat.send_message(user_msg)
    return response.text