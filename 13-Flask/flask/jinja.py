# Building Url Dynamically
# Variable Rule
# Jinja 2 Template Engine

# Jinja2 Template Engine
'''
{{  }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''

from flask import Flask,render_template,request,redirect,url_for
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
# WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"



# Variable Rule
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    
    exp={'score':score,"res":res}

    return render_template('result1.html',results=exp)

# if condition
@app.route('/sucess/<int:score>')
def success(score):
    return render_template('result.html',results=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',results=score)

@app.route('/form')
def form():
    return render_template('getresult.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method =='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science + maths + c + data_science) / 4

        if total_score >= 50:
            return redirect(url_for('success', score=total_score))
        else:
            return redirect(url_for('fail', score=total_score))

if __name__=="__main__":
    app.run(debug=True)

