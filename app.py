import streamlit as st
import os
from styles.css import apply_custom_css
from pages import welcome, upload, loading, results

st.set_page_config(page_title="Resumind AI", page_icon="✨", layout="wide", initial_sidebar_state="collapsed")

def init_session_state():
    if "page" not in st.session_state:
        st.session_state.page = "welcome"
    if "resume_path" not in st.session_state:
        st.session_state.resume_path = None
    if "resume_text" not in st.session_state:
        st.session_state.resume_text = ""
    if "analysis" not in st.session_state:
        st.session_state.analysis = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "job_description" not in st.session_state:
        st.session_state.job_description = ""

def main():
    init_session_state()
    apply_custom_css()
    
    page = st.session_state.page
    if page == "welcome":
        welcome.render()
    elif page == "upload":
        upload.render()
    elif page == "loading":
        loading.render()
    elif page == "results":
        results.render()

if __name__ == "__main__":
    main()