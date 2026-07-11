import streamlit as st
from components.charts import render_gauge
from utils.pdf_report import generate_report
from services.gemini_service import get_chat_response
import os

def render():
    data = st.session_state.analysis
    if not data:
        st.session_state.page = "upload"
        st.rerun()
        
    st.markdown("<h2 class='text-gradient'>Executive Dashboard</h2>", unsafe_allow_html=True)
    
    # 1. Metric Cards
    c1, c2, c3 = st.columns(3)
    with c1: render_gauge(data.get("resume_score", 0), "Overall Score")
    with c2: render_gauge(data.get("ats_score", 0), "ATS Match")
    with c3:
        st.markdown(f"""
        <div class='glass-card' style='height: 250px; display: flex; flex-direction: column; justify-content: center; align-items: center;'>
            <h3 style='color: #94a3b8; margin: 0;'>Resume Health</h3>
            <h2 class='text-gradient' style='font-size: 2.5rem; margin: 10px 0;'>{data.get("resume_health", "Unknown")}</h2>
        </div>
        """, unsafe_allow_html=True)
        
    st.divider()
    
    # 2. Layout
    col_main, col_side = st.columns([2, 1])
    
    with col_main:
        st.markdown("### Executive Summary")
        for item in data.get("summary", []):
            st.markdown(f"- {item}")
            
        st.markdown("### Strengths & Weaknesses")
        sc1, sc2 = st.columns(2)
        with sc1:
            for s in data.get("strengths", []): st.success(s)
        with sc2:
            for w in data.get("weaknesses", []): st.error(w)
            
        st.markdown("### Career Recommendations")
        for rec in data.get("career_recommendations", []):
            st.markdown(f"""
            <div class='glass-card' style='margin-bottom: 10px;'>
                <h4>{rec.get('role', '')} <span style='float:right; color:#3b82f6;'>{rec.get('match', 0)}% Match</span></h4>
                <p style='color: #94a3b8;'>{rec.get('reason', '')}</p>
            </div>
            """, unsafe_allow_html=True)
            
    with col_side:
        st.markdown("### Skills Analysis")
        st.markdown("**Found:**")
        st.markdown(" ".join([f"`{s}`" for s in data.get("skills_found", [])]))
        st.markdown("**Missing:**")
        st.markdown(" ".join([f"`{s}`" for s in data.get("missing_skills", [])]))
        
        st.divider()
        st.markdown("### Download Report")
        if st.button("Generate PDF", use_container_width=True):
            report_path = generate_report(data, "assets/uploads/report.pdf")
            with open(report_path, "rb") as f:
                st.download_button("Download PDF", f, file_name="Resumind_Report.pdf", mime="application/pdf", use_container_width=True)
        
        st.divider()
        if st.button("Start New Analysis", use_container_width=True):
            st.session_state.clear()
            st.rerun()

    st.divider()
    
    # 3. AI Chat Section
    st.markdown("### Resume AI Assistant")
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            
    prompt = st.chat_input("Ask anything about this resume...")
    if prompt:
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
            
        with st.chat_message("model"):
            with st.spinner("Thinking..."):
                try:
                    reply = get_chat_response(st.session_state.chat_history[:-1], prompt, str(data))
                    st.write(reply)
                    st.session_state.chat_history.append({"role": "model", "content": reply})
                except Exception as e:
                    st.error(f"Chat error: {str(e)}")