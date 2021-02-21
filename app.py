from flask import Flask, render_template, url_for, request 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/tracker", methods=['GET', 'POST'])
def tracker():
    return render_template('tracker.html')

@app.route("/timer", methods=['GET', 'POST'])
def timer():
    return render_template('timer.html')

if __name__ == "__main__":
    app.run()