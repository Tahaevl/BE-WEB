from flask import session
from ..model import bdd
import hashlib

def verifAuth(mail, mdp):
    session.clear()
    mdp=hashlib.sha256(mdp.encode())
    mdpC=mdp.hexdigest()
    msg, user=bdd.verifAuthData(mail, mdpC)
    print(msg)
    try:
        session["idUser"]=user["idUser"]
        session["nom"]=user["nom"]
        session["prenom"]=user["prenom"]
        session["mail"]=user["mail"]
        session["statut"]=user["statut"]
        info=msg
    except TypeError as err:
        info="authEchec"
        print("Failed verifAuth : {}".format(err))
    return info