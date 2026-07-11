import plotly.graph_objects as go
import streamlit as st

def render_gauge(value: int, title: str):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = value,
        title = {'text': title, 'font': {'color': 'white'}},
        gauge = {
            'axis': {'range': [None, 100], 'tickcolor': 'white'},
            'bar': {'color': "#3b82f6"},
            'bgcolor': "rgba(0,0,0,0)",
            'steps': [
                {'range': [0, 50], 'color': "rgba(239, 68, 68, 0.3)"},
                {'range': [50, 80], 'color': "rgba(245, 158, 11, 0.3)"},
                {'range': [80, 100], 'color': "rgba(16, 185, 129, 0.3)"}
            ]
        }
    ))
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", font={'color': "white"}, height=250)
    st.plotly_chart(fig, use_container_width=True)