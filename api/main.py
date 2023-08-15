from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def Sample():
    return jsonify({
        "Status" : "Success",
        "Text" : "Hello World"
    }),200
    
@app.route("/test")
def Other():
    return jsonify({
        "Status" : "Success",
        "Text" : "Fire"
    }),200
    