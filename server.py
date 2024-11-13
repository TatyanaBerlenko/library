from flask import Flask, jsonify, request
from db import books

app = Flask(__name__)


@app.route('/hello')
def home():
    return 'Hello! Welcome to my library'
