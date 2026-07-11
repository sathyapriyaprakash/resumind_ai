import streamlit as st
import time
from services.resume_service import process_resume

def render():
    st.markdown("""
        <div style='text-align: center; padding: 100px;'>
            <h2 class='text-gradient'>AI is analyzing your profile...</h2>
            <p style='color: #94a3b8;'>Extracting skills, computing ATS match, and generating career insights.</p>
        </div>
    """, unsafe_allow_html=True)
    
    with st.spinner("Processing..."):
        try:
            text, analysis = process_resume(
                st.session_state.resume_path, 
                st.session_state.job_description
            )
            st.session_state.resume_text = text
            st.session_state.analysis = analysis
            st.session_state.page = "results"
            st.rerun()
        except Exception as e:
            st.error(f"Error during analysis: {str(e)}")
            if st.button("Go Back"):
                st.session_state.page = "upload"
                st.rerun()