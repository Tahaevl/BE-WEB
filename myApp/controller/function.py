from flask import session
from ..model import bdd
def verifAuth(mail, mdp):
    session.clear()
    msg, user=bdd.verifAuthData(mail, mdp)
    print(msg)
    try:
        session["idUser"]=user["idUser"]
        session["nom"]=user["nom"]
        session["prenom"]=user["prenom"]
        session["mail"]=user["mail"]
        session["statut"]=user["statut"]
        session["avatar"]=user["avatar"]
        info=msg
    except TypeError as err:
        info="authEchec"
        print("Failed verifAuth : {}".format(err))
    return info