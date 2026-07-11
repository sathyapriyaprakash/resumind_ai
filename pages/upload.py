import os
import streamlit as st
from config import UPLOAD_DIR

def render():

    st.markdown(
        "<h2 class='text-gradient'>Upload Your Resume</h2>",
        unsafe_allow_html=True
    )
    st.info("""
         📱 **Mobile Users**

         If your resume is stored in **Google Drive**, please download it to your phone first.

        Then upload it from **Downloads** or **Files**.

        Direct upload from Google Drive may not work on some mobile browsers.
        """)
    jd = st.text_area(
        "Target Job Description (Optional)",
        placeholder="Paste the job description here..."
    )

    uploaded_file = st.file_uploader(
        "Drop your PDF resume here",
        type=["pdf"]
    )

    if uploaded_file is not None:

        st.success(f"✅ {uploaded_file.name} selected")

        if st.button("Analyze Resume", type="primary"):

            try:

                os.makedirs(UPLOAD_DIR, exist_ok=True)

                path = os.path.join(
                    UPLOAD_DIR,
                    uploaded_file.name
                )

                with open(path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                st.session_state.resume_path = path
                st.session_state.job_description = jd

                st.session_state.page = "loading"

                st.rerun()

            except Exception as e:

                st.error(str(e))