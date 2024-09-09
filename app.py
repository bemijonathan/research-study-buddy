from features import evaluate_paper
import streamlit as st
from analyzers import analyze_ai_solution
from enum import Enum


class Feature(Enum):
    ANALYZE_AI_SOLUTION = "Analyze AI Solution",
    EVALUATE_RESEARCH_PAPER = "Evaluate Research Paper",
    CONDUCT_AI_RESEARCH = "Conduct AI research"
    MARK_AI_RESEARCH = "Mark AI research"
    CREATE_POST_FROM_PAPER = "Create post from paper"


def main():
    st.title("AI Research Paper Analyzer and Evaluator")

    # Sidebar for feature selection
    feature = st.sidebar.selectbox(
        "Choose a feature",
        [f.value for f in Feature]
    )
    if feature == Feature.EVALUATE_RESEARCH_PAPER.value:
        evaluate_paper()
    elif feature == Feature.ANALYZE_AI_SOLUTION.value:
        analyze_ai_solution()


if __name__ == "__main__":
    main()
