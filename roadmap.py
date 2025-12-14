
def generate_roadmap(score):
    steps = []

    if score < 40:
        steps.append("Add README file")
        steps.append("Improve folder structure")

    if score < 70:
        steps.append("Write unit tests")
        steps.append("Use proper commit messages")

    if score >= 70:
        steps.append("Add CI/CD pipeline")
        steps.append("Improve documentation")

    return steps
