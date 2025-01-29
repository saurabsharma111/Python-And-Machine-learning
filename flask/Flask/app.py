from flask import Flask

#create instance of flask class
#wsgi app
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my first Flaskafv App"

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