from flask import Flask, render_template, request
from analyzers.bug_analyzer import analyze_code

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    code = ""

    if request.method == "POST":
        code = request.form.get("code", "")
        result = analyze_code(code)

    return render_template(
        "index.html",
        result=result,
        code=code
    )


if __name__ == "__main__":
    app.run(debug=True)