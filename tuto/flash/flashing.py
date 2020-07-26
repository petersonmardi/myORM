from flask import (Flask, 
render_template, redirect, url_for, request, flash)

app = Flask(__name__)
app.secret_key = 'abc'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['pass'] != 'jpt':
            error = 'invalid password'
        else:
            flash('You are successfully logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
