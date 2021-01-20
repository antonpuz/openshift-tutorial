from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello')
def hello():
    return 'That is the second important page'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Hello %s' % username