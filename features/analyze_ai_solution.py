import streamlit as st
from analyzers import extract_equations, validate_equations, extract_methodology, reproduce_results
from utils.openai_helper import generate_text


def analyze_solution():
    with st.form("analyze ai case study"):
        text = st.text_area("Describe the AI solution you wish to implement")
        drop_down = st.selectbox("Solution", [
            "AWS", "GCP", "Hugging face", "Native", "Open source model", "Generative AI"
        ])
        st.form_submit_button('Analyze')

    task = """Analyze the given ai case study for an applied AI solution. 
    1. Identify the main AI techniques or algorithms used.
    2. Summarize the key components of the solution base on the selected approach.
    3. create an Outline steps to implement this solution with #{drop_down} method.
    4. using the faker library provide a psuedo code for the user to get fake datasets 
    add instructions on the amount of data he can produce
    5. provide a detailed breakdown of how this problem can be solved include code if needed."""
    if text:
        result = generate_text([
            {"role": "system", "content": "You are an AI research paper analyzer and AWS solution architect. Provide detailed, well-structured analyses with citations where possible."},
            {
                "role": "user",
                "content": f"As a #{drop_down} AI specialist, #{task} \n ----\n here find the case study \n ---\n #{text}"
            },
        ])
        st.write(result)


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
    ai_solution_analysis = analyze_solution(text)
    st.subheader("AI Solution Analysis and AWS Implementation")
    st.write(ai_solution_analysis)

    # Reproduce results (if applicable)
    if st.button("Attempt to Reproduce Results"):
        results = reproduce_results(methodology)
        st.subheader("Reproduced Results")
        st.write(results)
