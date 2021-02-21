from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/profile")
def profile():
    return render_template('profile.html')


@app.route("/resources")
def resources():
    return render_template('resources.html')


@app.route("/tracker", methods=['GET', 'POST'])
def tracker():
    return render_template('tracker.html')


@app.route("/timer", methods=['GET', 'POST'])
def timer():
    return render_template('timer.html')


@app.route("/timerv2", methods=['GET', 'POST'])
def timer2():
    return render_template('timerv2.html')


if __name__ == "__main__":
    app.run()
