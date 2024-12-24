from flask import Flask, request, jsonify, render_template
from togetherai import TogetherAI


app = Flask(__name__)

@app.route("/", method=["GET"])
def home():
    return render_template("index.html")