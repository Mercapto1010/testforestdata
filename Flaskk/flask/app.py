from flask import Flask
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this best Flask course. This is an amazing course."

@app.route("/index")
def index():
    return "Welcome to the index page"
if __name__ == '__main__':
    app.run(debug=True)    #Debug = True se apne aap update ho jaata hai page only you have to refresh it
