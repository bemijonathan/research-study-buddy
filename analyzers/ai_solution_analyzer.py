import streamlit as st
from utils import analyze_text


def analyze_ai_solution():
    text = st.text_area("describe the AI solution you wish to implement")
    task = """Analyze the given text for an applied AI solution. 
    1. Identify the main AI techniques or algorithms used.
    2. Summarize the key components of the solution.
    3. Outline steps to implement this solution on AWS, including specific AWS services to use.
    4. Provide a high-level pseudocode or architecture for implementing this in AWS Cloud"""
    return analyze_text(text, task)
