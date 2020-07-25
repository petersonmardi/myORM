from flask import redirect, Flask, url_for, request, render_template, abort

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/validate', methods=['POST'])
def validate():
    if request.method == 'POST' and request.form['pass'] == 'jpt':
        return redirect(url_for('success'))
    # return redirect(url_for('login'))
    else:
        abort(401)

@app.route('/success')
def success():
    return 'logged in successfully'