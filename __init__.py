import sqlite3
from flask import Flask, g, render_template

app = Flask(__name__)

DATABASE = "./database/database.db"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def make_dicts(cursor, row):
    return dict((cursor.decription[idx][0], values)
                for idx, value in enumerate(row))

    db.row_factory = make_dicts

# Initial schemas
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read().decode('utf8'))
        db.commit()

@app.route("/")
def index():
    cur = get_db().cursor()
    cur.execute("insert into huawei_net values (1, '14-7-2020', 250.00, 'efectivo', '21', 'Sophonie', '10:f1:f2:1c:02:ee')")
    return render_template('index.html', c="Bonjou!")
