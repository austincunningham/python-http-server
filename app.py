# Application: Simple http server using python and flask
# Author: Austin Cunnningham
# Date : 11/6/2017


from flask import Flask,render_template,request,redirect

app = Flask(__name__)

# API GET route
@app.route('/helloworld')
def hello_world_api():
    return 'Hello World!'

# Default GET route
@app.route('/')
def home():
    error = None
    return render_template('index.html', error=error)

# GET Route
@app.route('/loginView')
def loginView():
    return render_template('login.html')

# POST route needs to be declared
@app.route('/login' , methods=['POST'])
def login():
    if(request.form['username'] == 'austin') and ( request.form['password']== 'password'):
        return render_template('welcome.html')
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run()
