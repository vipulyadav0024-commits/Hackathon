
def calculate_score(data):
    score = 0

    if data.get("description"):
        score += 10
    if data.get("language"):
        score += 10
    if data.get("stargazers_count", 0) > 0:
        score += 10
    if data.get("forks_count", 0) > 0:
        score += 10

    return score
