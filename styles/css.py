import streamlit as st
from .theme import COLORS

def apply_custom_css():
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
        
        * {{ font-family: 'Inter', sans-serif; }}
        
        .stApp {{
            background: radial-gradient(circle at 15% 50%, rgba(20, 30, 60, 1), {COLORS['background']} 40%),
                        radial-gradient(circle at 85% 30%, rgba(30, 20, 60, 1), {COLORS['background']} 40%);
            background-color: {COLORS['background']};
            color: {COLORS['text_main']};
        }}
        
        /* Hide Streamlit Header */
        header {{ visibility: hidden; }}
        #MainMenu {{ visibility: hidden; }}
        footer {{ visibility: hidden; }}
        
        /* Glassmorphism Cards */
        .glass-card {{
            background: {COLORS['card_bg']};
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid {COLORS['card_border']};
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        .glass-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 12px 40px 0 {COLORS['primary_glow']};
        }}
        
        /* Gradient Text */
        .text-gradient {{
            background: linear-gradient(90deg, #60a5fa, #a78bfa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        /* Buttons */
        .stButton>button {{
            background: linear-gradient(135deg, #3b82f6, #2563eb);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            transition: all 0.3s;
        }}
        .stButton>button:hover {{
            box-shadow: 0 0 15px {COLORS['primary_glow']};
            transform: scale(1.02);
        }}
    </style>
    """, unsafe_allow_html=True)