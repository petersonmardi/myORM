from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "Index page"

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/user/<username>")
def show_user_profile(username):
    return "{}".format(escape(username))

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"{post_id}"
