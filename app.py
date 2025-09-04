from flask import Flask, render_template
import data_fetch as fetch
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    data = fetch.file_data
    date = datetime.datetime.now().strftime("%d-%m-%Y")
    return render_template("index.html", data = data, date = date)

if __name__ == "__main__":
    app.run(host="localhost", port=8080)
