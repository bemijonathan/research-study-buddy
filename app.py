import streamlit as st
from utils import extract_text_from_pdf
from analyzers import (
    extract_equations, validate_equations,
    extract_methodology, reproduce_results,
    analyze_ai_solution
)
from evaluators import (
    extract_paper_info,
    extract_research_question,
    extract_results,
    extract_conclusions,
    evaluate_paper
)


def main():
    st.title("AI Research Paper Analyzer and Evaluator")

    # File upload
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        # Extract text from PDF
        text = extract_text_from_pdf(uploaded_file)

        # Sidebar for feature selection
        feature = st.sidebar.selectbox(
            "Choose a feature",
            (
                "Evaluate Research Paper",
                "Analyze AI Solution",
                "Conduct AI research",
                "Mark AI research",
                "Create post from paper"
            )
        )

        if feature == "Evaluate Research Paper":
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

        elif feature == "Analyze AI Solution":
            st.header("AI Solution Analysis")

            # Extract equations
            equations = extract_equations(text)
            st.subheader("Extracted Equations")
            st.write(equations)

            # Validate equations
            validation_results = validate_equations(equations)
            st.subheader("Equation Validation Results")
            st.write(validation_results)

            # Extract methodology
            methodology = extract_methodology(text)
            st.subheader("Extracted Methodology")
            st.write(methodology)

            # Analyze AI solution and provide AWS implementation steps
            ai_solution_analysis = analyze_ai_solution(text)
            st.subheader("AI Solution Analysis and AWS Implementation")
            st.write(ai_solution_analysis)

            # Reproduce results (if applicable)
            if st.button("Attempt to Reproduce Results"):
                results = reproduce_results(methodology)
                st.subheader("Reproduced Results")
                st.write(results)


if __name__ == "__main__":
    main()
