
import requests
from scorer import calculate_score
from roadmap import generate_roadmap

def analyze_repo(repo_url):
    parts = repo_url.replace("https://github.com/", "").split("/")
    owner = parts[0]
    repo = parts[1]

    api = f"https://api.github.com/repos/{owner}/{repo}"
    data = requests.get(api).json()

    score = calculate_score(data)
    roadmap = generate_roadmap(score)

    summary = "Good project but needs improvement."

    return {
        "score": score,
        "summary": summary,
        "roadmap": roadmap
    }
