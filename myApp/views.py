from flask import Flask, redirect, render_template, request, session
from .model import bdd as bdd
from .controller import function as f
import hashlib

app = Flask(__name__)
app.template_folder = 'template'
app.static_folder = 'static'
app.config.from_object('myApp.config')


@app.route('/')
@app.route('/index')
@app.route('/index/<infoMsg>')
def index(infoMsg=""):
    return render_template('index.html',info=infoMsg)


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
    
@app.route('/inscription',methods=['POST'])
def inscription():
    nom=request.form['nom']
    prenom=request.form['prenom']
    mail=request.form['mail']
    mdp=request.form['password']
    mdp = hashlib.sha256(mdp.encode()) 
    mdpC = mdp.hexdigest()
    statut=-1
    msg=bdd.add_membreData(nom,prenom,mail,mdpC,statut)
    if msg=="addMembreOK":
        return redirect("/index/addMembreOK")
    else:
        return redirect("/index/addMembreError")
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect("/index/logoutOK")

@app.route("/membre")
@app.route("/membre/<infoMsg>")
def membre(infoMsg=''):
    msg,listeMembre = bdd.get_membreData()
    print(msg)
    return render_template("membre.html",liste=listeMembre, infoErr=msg, info=infoMsg)
    
@app.route("/suppMembre")
def suppMembre():
    idUser = request.args.get("userDel")
    msg = bdd.del_membreData(idUser)
    print(msg)
    if msg == "suppMembreOK":
        return redirect("/membre/delOK")
    else:
        return redirect("/membre/delProblem")
    
@app.route("/updateMembre", methods=['POST'])
def updateMembre():
    idUser = request.form['pk']
    champ = request.form['name']
    newvalue = request.form['value']
    msg = bdd.update_membreData(champ, idUser, newvalue)
    print(msg)
    return msg