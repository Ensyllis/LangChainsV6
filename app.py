from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    current_time = datetime.datetime.now()
    this_time = current_time.strftime('%H:%M:%S')
    return render_template("index.html", year = this_time)

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)