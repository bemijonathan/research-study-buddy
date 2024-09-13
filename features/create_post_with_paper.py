import streamlit as st
import requests
from typing import List, Dict
from utils.openai_helper import generate_text


class CreatePostWithPaper:
    @staticmethod
    def search_papers(query: str, limit: int = 10) -> List[Dict]:
        # Placeholder for paper search functionality
        # Replace with actual API calls to academic databases
        papers = [
            {"title": f"Paper {i}", "abstract": f"Abstract {
                i}", "conclusion": f"Conclusion {i}"}
            for i in range(limit)
        ]
        return papers

    @staticmethod
    def extract_facts_from_abstract(abstract: str, num_facts: int = 3) -> List[str]:
        # Placeholder for fact extraction
        # Replace with NLP techniques for better results
        facts = abstract.split(". ")[:num_facts]
        return facts

    @staticmethod
    def extract_quotes_from_conclusion(conclusion: str, num_quotes: int = 1) -> List[str]:
        # Placeholder for quote extraction
        # Replace with NLP techniques for better results
        quotes = conclusion.split(". ")[:num_quotes]
        return quotes

    @staticmethod
    def create_post(paper: Dict, platform: str, tone: str, facts: List[str], quotes: List[str], add_examples: bool) -> str:
        prompt = f"Create a {platform} post about the research paper titled '{
            paper['title']}'. "
        prompt += f"Include the following facts from the abstract: {
            ', '.join(facts)}. "
        prompt += f"Use the following quote(s) from the conclusion: {
            ', '.join(quotes)}. "
        prompt += f"The tone should be {tone}. "

        if add_examples:
            prompt += "Please add relevant examples to illustrate the points."

        post_content = generate_text(prompt)
        return post_content

    @staticmethod
    def show_paper():
        st.title("Create Post from Research Paper")

        # Input for paper search
        query = st.text_input("Enter keywords to search for papers:")
        search_button = st.button("Search Papers")

        if search_button and query:
            papers = CreatePostWithPaper.search_papers(query)
            if papers:
                selected_paper = st.selectbox(
                    "Select a paper:", [p['title'] for p in papers])
                paper = next(p for p in papers if p['title'] == selected_paper)

                st.subheader("Paper Details")
                st.write(f"Title: {paper['title']}")
                st.write(f"Abstract: {paper['abstract']}")
                st.write(f"Conclusion: {paper['conclusion']}")

                # Post creation options
                st.subheader("Create Post")
                platform = st.selectbox("Select platform:", [
                                        "LinkedIn", "Twitter", "Facebook"])
                tone = st.selectbox(
                    "Select tone:", ["Professional", "Casual", "Academic", "Enthusiastic"])
                num_facts = st.slider("Number of facts to include:", 1, 5, 3)
                num_quotes = st.slider("Number of quotes to include:", 1, 3, 1)
                add_examples = st.checkbox("Add examples to the post")

                if st.button("Generate Post"):
                    facts = CreatePostWithPaper.extract_facts_from_abstract(
                        paper['abstract'], num_facts)
                    quotes = CreatePostWithPaper.extract_quotes_from_conclusion(
                        paper['conclusion'], num_quotes)
                    post_content = CreatePostWithPaper.create_post(
                        paper, platform, tone, facts, quotes, add_examples)

                    st.subheader("Generated Post")
                    st.text_area("Post content:",
                                 value=post_content, height=300)
            else:
                st.warning("No papers found for the given query.")
