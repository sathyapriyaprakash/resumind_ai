import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Read from .env (local)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# If not found, read from Streamlit Secrets (Cloud)
if not GEMINI_API_KEY:
    GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("Missing GEMINI_API_KEY in environment.")

MODEL_NAME = "gemini-2.0-flash"

UPLOAD_DIR = "assets/uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)