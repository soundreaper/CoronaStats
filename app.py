import os
from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/mypage.jpg', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    """Index page of the application"""
    return render_template('index.html')

@app.route('/login')
def login():
    """Page for logging in"""
    return render_template('login.html')

@app.route('/register')
def register():
    """Page for registering"""
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)