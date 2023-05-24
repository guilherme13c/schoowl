from flask import Flask, session, redirect, url_for, request
from database_interface import *

db = DB()

app = Flask(__name__)

@app.get("/")
def test_api():
    return {
        "Message": "Working"
    }

@app.post("/login")
def login_api():
    pass

if (__name__ == "__main__"):
    app.run(host="0.0.0.0", port=5000)
