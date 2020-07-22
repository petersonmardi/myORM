from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("post.html", v="Welcome")
    
@app.route("/login", methods=['POST'])
def login():
    uname = request.form['uname']
    password = request.form['pass']
    if uname == "peterson" and password == "mardi":
        return f"Welcome {uname}"
