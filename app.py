
from flask import Flask, render_template, request
from analyzer import analyze_repo

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        repo_url = request.form["repo"]
        result = analyze_repo(repo_url)
        return render_template("index.html", result=result)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
