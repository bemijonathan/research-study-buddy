from utils.openai_helper import analyze_text


def extract_methodology(text):
    task = "Extract and summarize the methodology described in the given text."
    return analyze_text(text, task)
