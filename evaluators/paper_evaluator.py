from utils import analyze_text


def extract_paper_info(text):
    task = "Extract basic information like title, authors, publication date, and journal from the given text."
    return analyze_text(text, task)


def extract_research_question(text):
    task = "Identify the main research question and hypothesis of the paper."
    return analyze_text(text, task)


def extract_results(text):
    task = "Extract the key results and findings from the paper."
    return analyze_text(text, task)


def extract_conclusions(text):
    task = "Identify the main conclusions and their implications from the paper."
    return analyze_text(text, task)


def evaluate_paper(text):
    task = "Assess the overall quality, contribution, and limitations of the paper."
    return analyze_text(text, task)
