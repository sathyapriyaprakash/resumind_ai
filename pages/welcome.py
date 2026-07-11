import streamlit as st

def render():
    st.markdown("""
        <div style='text-align: center; padding: 100px 20px;'>
            <h1 class='text-gradient' style='font-size: 4rem; margin-bottom: 20px;'>Resumind AI</h1>
            <p style='font-size: 1.5rem; color: #94a3b8; max-width: 600px; margin: 0 auto 40px auto;'>
                Elevate your career with AI-driven resume analysis. Get ATS scoring, skill gap identification, and personalized roadmaps in seconds.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Get Started", use_container_width=True):
            st.session_state.page = "upload"
            st.rerun()