from flask import Flask

app = Flask(__name__)

@app.route("/")
def start():
    return "MBSA's Flask Server Successfully started."


