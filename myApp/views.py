from flask import Flask, redirect, render_template, request, session
from .model import bdd
from .controller import function as f
app = Flask(__name__)
app.template_folder = 'template'
app.static_folder = 'static'
app.config.from_object('myApp.config')


@app.route('/')
@app.route('/index')
@app.route('/index/<infoMsg>')
def index(infoMsg=""):
    return render_template('index.html',info=infoMsg)

@app.route('/administration')
def blog():
    return render_template('administration.html')


@app.route('/sattelite/GPS')
def GPS():
    return render_template('sattelite-GPS.html')

@app.route('/login')
@app.route('/login/<infoMsg>')
def login(infoMsg=""):
    return render_template("login.html",info=infoMsg)

@app.route('/connecter', methods=["POST"])
def connecter():
    mail=request.form['mail']
    password=request.form['password']
    msg=f.verifAuth(mail , password)
    print(msg)
    if "idUser" in session:
        return redirect("/index/authOK")
    else:
        return redirect("/login/authEchec")
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect("/index/logoutOK")

    
