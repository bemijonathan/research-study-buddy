import streamlit as st
from evaluators import extract_paper_info, extract_research_question, extract_results, extract_conclusions
from utils import extract_text_from_pdf


def evaluate_paper() -> None:
    # File upload
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        # Extract text from PDF
        text = extract_text_from_pdf(uploaded_file)
        st.header("Research Paper Evaluation")
        # Extract paper info
        paper_info = extract_paper_info(text)
        st.subheader("Paper Information")
        st.write(paper_info)

        # Extract research question
        research_question = extract_research_question(text)
        st.subheader("Research Question and Hypothesis")
        st.write(research_question)

        # Extract results
        results = extract_results(text)
        st.subheader("Key Results and Findings")
        st.write(results)

        # Extract conclusions
        conclusions = extract_conclusions(text)
        st.subheader("Main Conclusions and Implications")
        st.write(conclusions)

        # Evaluate paper
        evaluation = evaluate_paper(text)
        st.subheader("Paper Evaluation")
        st.write(evaluation)
