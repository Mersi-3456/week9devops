
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name", "").strip()
    password = request.form.get("password", "")
    number = request.form.get("Number", "")

    if not name or not password or len(password) < 6 or not number:
        return "Invalid input. Please return and enter valid details.", 400

    return render_template("successful.html", name=name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
