from flask import *
from flask-mail import *

app = Flask(__name__)

#flask mail configuration
app.config['Mail_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='petersonmardi@gmail.com'
app.config['MAIL_PASSWORD']='12345'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

#instatiate the Mail
mail = Mail(app=app)

#configure the Message class object and send email from a URL

@app.route('/')
def index():
    msg = Message('subject',sender='admin@gmail.com', recipients=['username@gmail.com'])
    msg.body = 'Hi, this is the email sent by using the flask web application'
    return 'Mail sent, please check the mail id'