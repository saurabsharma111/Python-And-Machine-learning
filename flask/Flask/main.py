from flask import Flask
from flask import render_template

#create instance of flask class
#wsgi app
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1> to my first Flask App</h1><html>"

@app.route("/index")
def index():
    return "Welcome to my index App"

@app.route("/contact")
def contact():
    return "Welcome to my contact App"
#execution of code will start from here
if __name__ =='__main__':
    #debug=True will make real time changes
    app.run(debug=True)