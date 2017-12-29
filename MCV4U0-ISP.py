import os
from flask import Flask, request

app = Flask(__name__) # Create application instance.

@app.route("/")
def index():
	# Home page
