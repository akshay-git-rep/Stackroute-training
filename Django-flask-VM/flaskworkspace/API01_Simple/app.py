from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def SayHello():
    return({'messgae': 'Hello World from Flask App'})

@app.route("/hi")
def SayHi():
    return({'messgae': 'Hi from Flask App'})

@app.route("/error")
def CheckError():
    return 10/0
