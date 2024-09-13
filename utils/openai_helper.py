import openai
from openai import OpenAI
import os
from dotenv import load_dotenv
from typing import List, Dict, Literal
from scholarly import scholarly
import requests
from bs4 import BeautifulSoup

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_text(text, task, model='gpt-3.5-turbo-16k'):
    # "gpt-4-turbo-preview"
    try:
        response = client.chat.completions.create(
            model=model,  # Using the latest model for better performance
            messages=[
                {"role": "system", "content": "You are an AI research paper analyzer and AWS solution architect. Provide detailed, well-structured analyses with citations where possible."},
                {"role": "user", "content": f"Task: {
                    task}\n\nAnalyze the following research paper text:\n\n{text}"}
            ],
            max_tokens=2000,  # Increased for more comprehensive analysis
            temperature=0.7,  # Adjusted for a balance of creativity and consistency
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].message.content
    except openai.APIError as e:
        return f"Error in API call: {str(e)}"


def generate_text(messages: List[Dict[Literal["role", "content"], str]], model='gpt-3.5-turbo-16k'):
    try:
        response = client.chat.completions.create(
            model=model,  # Using the latest model for better performance
            messages=messages,
            max_tokens=2000,  # Increased for more comprehensive analysis
            temperature=0.7,  # Adjusted for a balance of creativity and consistency
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].message.content
    except Exception as e:
        print(e)
        return "Error occurred"


class ResearchAgent:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = self.api_key

    def search_papers(self, topic: str, num_papers: int = 10) -> List[Dict]:
        search_query = scholarly.search_pubs(topic)
        papers = []
        for i in range(num_papers):
            try:
                paper = next(search_query)
                papers.append({
                    'title': paper['bib']['title'],
                    'authors': ', '.join(paper['bib']['author']),
                    'year': paper['bib'].get('pub_year', 'N/A'),
                    'abstract': paper['bib'].get('abstract', 'N/A'),
                    'url': paper['pub_url']
                })
            except StopIteration:
                break
        return papers

    def summarize_paper(self, paper: Dict) -> str:
        prompt = f"Summarize the key points of the paper titled '{
            paper['title']}' by {paper['authors']}."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a research assistant."},
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']

    def get_full_text(self, url: str) -> str:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # This is a simple extraction and might need to be adjusted based on the website structure
        text = soup.get_text()
        return text[:5000]  # Limiting to first 5000 characters for brevity

    def _parse_papers(self, content: str) -> List[Dict]:
        # Parse the content to extract paper information
        # This is a simplified version and may need to be adjusted based on the actual output format
        papers = []
        lines = content.split('\n')
        for line in lines:
            if line.startswith('Title:'):
                paper = {'title': line.split('Title:')[1].strip()}
            elif line.startswith('Authors:'):
                paper['authors'] = line.split('Authors:')[1].strip()
            elif line.startswith('Year:'):
                paper['year'] = line.split('Year:')[1].strip()
                papers.append(paper)
        return papers


class OpenAIHelper:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = self.api_key

    def analyze_text(self, text, task, model='gpt-3.5-turbo-16k'):
        return analyze_text(text, task, model)

    def create_research_agent(self) -> ResearchAgent:
        return ResearchAgent(self.api_key)
