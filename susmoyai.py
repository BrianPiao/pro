from flask import Flask

#flask object
app = Flask(__name__)
#use route() decorator to tell Flask what URL should trigger our function.

@app.route("/")
def hello_world():
     return "i dont want you here"

@app.route("/yes")
def get_out():
    return "get outta here"


if(__name__ == "__main__"):
     app.run(debug = True ,  port = 8000)