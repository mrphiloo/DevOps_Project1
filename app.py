from flask import Flask

app = Flask(__name__)

@app.route("/info")
def lwinfo():
	return "I am Venkata Ramana"

@app.route("/phone")
def lwphone():
	return "95738097"

app.run(host="0.0.0.0")
