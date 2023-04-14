from flask import Flask, render_template, request, make_response, redirect, url_for
from atprototools import Session
import os

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    username = request.cookies.get("username")
    password = request.cookies.get("password")
    if not (username and password):
        return redirect(url_for("settings"))
    else:
        return render_template("index.html")

@app.route("/followprofile")
def index_follow():
    username = request.cookies.get("username")
    password = request.cookies.get("password")
    if not (username and password):
        return redirect(url_for("settings"))
    else:
        return render_template("follow.html")

@app.route("/post", methods=["POST"])
def post_skoot():
    username = request.form.get("username")
    password = request.form.get("password")
    post_content = request.form.get("post-content")
    bsky = Session(username, password)
    bsky.post_skoot(post_content)
    return "Posted to BlueSky successfully!"

@app.route("/skootpost", methods=["POST"])
def post_skoot_bsky():
    username = request.cookies.get("username")
    password = request.cookies.get("password")
    post_content = request.form.get("post-content")
    bsky = Session(username, password)
    bsky.post_skoot(post_content)
    return "Posted to BlueSky successfully!"

@app.route("/follow_repo", methods=["POST"])
def follow_user_bsky():
    username = request.cookies.get("username")
    password = request.cookies.get("password")
    followuser = request.form.get("profile")
    bsky = Session(username, password)
    bsky.follow(followuser)
    return "Followed user successfully!"

@app.route("/follow", methods=["POST"])
def follow_profile():
    username = request.form.get("username")
    password = request.form.get("password")
    profile = request.form.get("profile")
    bsky = Session(username, password)
    bsky.follow(profile)
    return "Followed user successfully!"


@app.route("/settings", methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        resp = make_response(render_template("settings.html", saved=True))
        resp.set_cookie("username", username)
        resp.set_cookie("password", password)
        return resp
    else:
        username = request.cookies.get("username")
        password = request.cookies.get("password")
        return render_template("settings.html", username=username, password=password)


@app.route("/latest-skoots")
def latest_skoots():
    username = request.cookies.get("username")
    password = request.cookies.get("password")
    bsky = Session(username, password)
    latest_skoots = bsky.get_latest_n_skoots(username, 1).content
    return render_template("latestskoots.html", latest_skoots=latest_skoots)

@app.route("/did")
def getdid():
    username = request.cookies.get("username")
    password = request.cookies.get("password")
    bsky = Session(username, password)
    yourdid = bsky.DID
    return yourdid


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
