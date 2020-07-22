from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login_example.html", v="Welcome to flask app!")

@app.route("/login_example", methods=['GET'])
def login_example():
    uname = request.args.get('uname')
    password = request.args.get('pass')
    post = request.args.get('name')
    if uname=="peterson" and password=="mardi":
        return f"User: {uname} - {post}!"
