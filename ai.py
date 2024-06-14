from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    user_input = request.form["user_input"]
    command = f"tgpt '{user_input}'"

    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode("utf-8")
    except subprocess.CalledProcessError as e:
        return "Error: " + e.output.decode("utf-8")


if __name__ == "__main__":
    app.run(debug=True)
