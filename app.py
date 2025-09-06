from flask import Flask, render_template
import data_fetch as fetch

app = Flask(__name__)

@app.route("/")
def home():
    data = fetch.file_data
    date = fetch.date
    return render_template("index.html", data = data, date = date)

if __name__ == "__main__":
    app.run(host="localhost", port=8080)
