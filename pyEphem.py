from asyncio.windows_events import NULL
from unicodedata import category
import ephem as ep
import math
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="yourusername",password="yourpassword",database="mydatabase")
Gearth = 3.986004418*10**14


def tle(file):
    f = open(file,'r')
    L = f.readlines()
    n = len(L)

    for i in range(0,n//3,3):
        sky = {}
    
        sky[L[i]]=ep.readtle(L[i],L[i+1],L[i+2])
    f.close()
    return sky

def insert(dic):
    for x,y in dic.items() :
        ids = 1
        category = "{}".format(dic)
        n = float(y.n)*2*math.pi/86400
        semiMinorAxis = (n**2*Gearth)**(1/3)
        e = y.e
        semiMajorAxis = semiMinorAxis*(1-e**2)**(1/2)
        mydb.execute("INSERT INTO table (idSatelitte ,nomSatelitte ,category ,orbite ,longitude ,latitude ,altitude ,inclinaison ,longitudeNoeud ,anomalieMoyenne ,semiMajorAxis ,semiMinorAxis ,arg ,source ,idUser, idPays) VALUES (:idSatelitte ,:nomSatelitte ,:category ,:orbite ,:longitude ,:latitude ,:altitude ,:inclinaison ,:longitudeNoeud ,:anomalieMoyenne ,:semiMajorAxis ,:semiMinorAxis ,:arg ,:source ,:idUser, :idPays)", [ids,x,category,y.orbit,y.lon,y.lat,y.elevation,y.inc,y._Om,y._M, semiMajorAxis,semiMinorAxis, y.ap, 'celestrak',NULL,NULL ])
        ids +=1





