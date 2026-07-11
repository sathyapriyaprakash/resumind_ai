import streamlit as st

def render():
    analysis = st.session_state.analysis
    st.subheader("🛠 Skills Found")
    st.write(", ".join(analysis.get("skills_found", [])))

    st.subheader("❌ Missing Skills")
    st.write(", ".join(analysis.get("missing_skills", [])))
