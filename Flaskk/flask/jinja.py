# Building Dynamic URL
# Variable Rule
# Jinja 2 template engine
### Jinja2 Template Engine
'''
{{  }} expressions to print output in html
{%...%} conditions, for loops     
{#...#} this is for comments
Basically ye upr jo 3 hain unse hm html file k andr apna code likh skte hain jo bhi cheeze apply krni hai kr skte hain
'''

from flask import Flask, render_template, request, redirect, url_for
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''

app = Flask(__name__)
@app.route("/")
def welcome():
    return "<html><H1>Welcome to the Flask Course</H2></html>"

@app.route("/index",methods = ['GET'])
def index():
    return render_template('index.html')     # Carefully write the name of folder as "templates"

@app.route("/about")
def about():
    return render_template('about.html')

# @app.route('/submit',methods = ['GET','POST'])
# def submit():
#     if request.method=='POST':
#         name=request.form['name']
#         return f'Hello {name}!'
#     return render_template('form.html')

# Variable rule
@app.route('/success/<int:score>')     # <> we use this to make variable 
def success(score):
    # return f"The marks you got is {score}" 
    # return "The marks you got is " + str(score)
    res = ""
    if score>=50:
        res = "PASSED"
    else:
        res = "FAILED"

    return render_template('result.html', results = res)

@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score>=50:
        res = "PASSED"
    else:
        res = "FAILED"
    exp = {"score": score, "res": res}
    return render_template('result1.html', results = exp)

#if condition
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html', results = score)


@app.route('/fail')
def fail(score):
     return render_template('result.html', results = score)

@app.route('/submit', methods = ['POST','GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science+maths+c+data_science)/4
    
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres', score=total_score))

if __name__ == "__main__":
    app.run(debug=True)    #Debug=True se apne aap update ho jaata hai page only you have to refresh it
