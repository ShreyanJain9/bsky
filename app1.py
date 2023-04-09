from flask import Flask, render_template, request
import atprototools as atpt
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/post", methods=["POST"])
def post_skoot():
    username = request.form.get("username")
    password = request.form.get("password")
    post_content = request.form.get("post-content")
    atpt.login(username, password)
    atpt.post_skoot(post_content)
    return "Posted to BlueSky successfully!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
