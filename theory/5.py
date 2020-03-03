from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! 123"

@app.route("/status")
def status():
    return {
        'status': True,
        'datetime': str(datetime.now())
    }

app.run()
