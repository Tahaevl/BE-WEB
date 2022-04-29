from flask import Flask, render_template, request
from .model import bdd
from .controller import function as f
app = Flask(__name__)
app.template_folder = 'template'
app.static_folder = 'static'
app.config.from_object('myApp.config')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog/sujet1')
def sujet1():
    return render_template('blog-sujet1.html')

@app.route('/sattelite/GPS')
def GPS():
    return render_template('sattelite-GPS.html')

@app.route('/login')
def authentification():
    return render_template("login.html")

@app.route('/connecter', methods=["POST"])
def connecter():
    print(request.form)
    mail=request.form['mail']
    password=request.form['password']
    verifAuthData(mail , password)
    

    
    