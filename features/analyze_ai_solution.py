import streamlit as st

from analyzers import extract_equations, validate_equations, extract_methodology, reproduce_results


def analyze_ai_solution(text: str) -> None:
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
