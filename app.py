
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/about')
def about():
    return 'This is about page'

@app.route('/login')
def login():
    return 'This is login page'

@app.route('/contact')
def contact(option="mail"):
    if option == "mail":
        return 'Enter your email here: <input type="text" name="email">'
    else:
        return 'This is contact page. \nWe are located at 1b James street, Kgn 5'
