from utils import analyze_text


def extract_equations(text):
    task = "Extract and list all mathematical equations from the given text."
    return analyze_text(text, task)
