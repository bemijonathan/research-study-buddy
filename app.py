from features import evaluate_paper, analyze_solution, CreatePostWithPaper
import streamlit as st
from enum import Enum


class Feature(Enum):
    ANALYZE_AI_SOLUTION = "Create AI Solution from use case"
    EVALUATE_RESEARCH_PAPER = "Evaluate Research Paper"
    CONDUCT_AI_RESEARCH = "Conduct AI research"
    MARK_AI_RESEARCH = "Mark AI research"
    CREATE_POST_FROM_PAPER = "Create post from paper"


def main():
    st.title("AI Research Paper Analyzer and Evaluator")

    # Sidebar for feature selection
    feature = st.sidebar.selectbox(
        "Choose a feature", [f.value for f in Feature])

    # if feature == Feature.EVALUATE_RESEARCH_PAPER.value:
    #     evaluate_paper()
    if feature == Feature.ANALYZE_AI_SOLUTION.value:
        analyze_solution()
    # elif feature == Feature.CREATE_POST_FROM_PAPER.value:
    #     CreatePostWithPaper.show_paper()


if __name__ == "__main__":
    main()
