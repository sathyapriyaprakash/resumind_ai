import streamlit as st
import os
from config import UPLOAD_DIR

def render():
    st.markdown("<h2 class='text-gradient'>Upload Your Resume</h2>", unsafe_allow_html=True)
    
    jd = st.text_area("Target Job Description (Optional)", placeholder="Paste the job description here to tailor the analysis...")
    
    uploaded_file = st.file_uploader("Drop your PDF resume here", type=["pdf"])
    
    if st.button("Analyze Resume", type="primary") and uploaded_file:
        path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        with open(path, "wb") as f:
            f.write(uploaded_file.getbuffer())
            
        st.session_state.resume_path = path
        st.session_state.job_description = jd
        st.session_state.page = "loading"
        st.rerun()