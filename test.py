from asyncio.windows_events import NULL
from unicodedata import category
import ephem as ep
import math as ma
import mysql.connector
import pymysql
from mysql.connector import errorcode

DB_SERVER = pymysql.connect(user="root", password="",host="localhost",database="test")
mycursor=DB_SERVER.cursor() 
Gearth = 3.986004418*(10**14)

###################################################################################
# connexion au serveur de la base de données

# def connexion():
#     cnx = ""
#     try:
#         cnx = pymysql.connect(DB_SERVER)
#         error=None
#     except pymysql.Error as err:
#         error=err
#         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#             print("Mauvais login ou mot de passe")
#         elif err.errno == errorcode.ER_BAD_DB_ERROR:
#             print("La Base de données n'existe pas.")
#         else:
#             print(err)
#     return cnx, error
    

#################################################################################
# fermeture de la connexion au serveur de la base de données

def close_bd(cursor, cnx):
    cursor.close()
    cnx.close()

#################################################################################
#Traitement du TLE

def tle(file):
    f = open(file,'r')
    L = f.readlines()
    n = len(L)
    sky = {}
    for i in range(0,n//3,3):    
        sky[L[i]]=ep.readtle(L[i],L[i+1],L[i+2])
    f.close()
    return sky

# Special-Interest Satellites

last_30_days = tle("C:\\Users\\Taha\\Desktop\\test\\Latest_30.txt")
# space_stations=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/space-stations.txt")
# brightest=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/visual.txt")
# active=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/active.txt")
# analyst=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/analyst.txt")
# cosmos_1408=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/1982-092.txt")
# microsat_r=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/2019-006.txt")
# fengyun_1c=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/1999-025.txt")
# iridium_33_debris=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/iridium-33-debris.txt")
# cosmos_2251_debris=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/cosmos-2251-debris.txt")

# # Weather and Earth Ressources Satellites
# weather=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/weather.txt")
# noaa=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/noaa.txt")
# goes=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/goes.txt")
# resource=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/resource.txt")
# sarsat=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/sarsat.txt")
# disaster_monitoring=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/dmc.txt")
# tdrss=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/tdrss.txt")
# argos=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/argos.txt")
# planet=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/planet.txt")
# spire=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/spire.txt")

# #Communications Satellites

# geosynchronous=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/geo.txt")
# gpz=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/gpz.txt")
# gpz_plus=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/gpz-plus.txt")
# intelsat=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/intelsat.txt")
# ses=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/ses.txt")
# iridium=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/iridium.txt")
# iridium_next=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/iridium-next.txt")
# starlink=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/starlink.txt")
# oneweb=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/oneweb.txt")
# orbcomm=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/orbcomm.txt")
# globalstar=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/globalstar.txt")
# swarm=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/swarm.txt")
# amateur_radio=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/amateur.txt")
# experimental_comm=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/x-comm.txt")
# other_comm=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/other-comm.txt")
# satnogs=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/satnogs.txt")
# gorizont=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/gorizont.txt")
# raduga=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/raduga.txt")
# molniya=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/molniya.txt")

# # Navigation Satellites

# gnss=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/gnss.txt")
# gps_ops=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/gps-ops.txt")
# glonass_ops=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/glo-ops.txt")
# galileo=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/galileo.txt")
# beidou=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/beidou.txt")
# sbas=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/sbas.txt")
# nnss=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/nnss.txt")
# russian_leo_navigation=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/musson.txt")

# # Scientific Satellites

# science=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/science.txt")
# geodetic=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/geodetic.txt")
# engineering=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/engineering.txt")
# education=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/education.txt")

# #Miscellaneous Satellites

# military=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/military.txt")
# radar=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/radar.txt")
# cubesat=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/cubesat.txt")
# other=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/other.txt")
 

def insert(dic):
    ids = 1
    for x,y in dic.items() :
        # try:
            # cnx, error = connexion()
            # cursor = cnx.cursor()
            # # suppression des données précédentes
            # sql1 = "TRUNCATE TABLE identification;"
            # cursor.execute(sql1)
            # insertion des nouvelles données
        category = NULL
        n = float(y.n)*2*ma.pi/86400
        semiMinorAxis = (n**2*Gearth)**(1/3)
        e = y.e
        semiMajorAxis = semiMinorAxis*(1-e**2)**(1/2)
        RA=y.raan #ascension droite de 0° à 360°
        if RA>180:
            RA-=360 #longitude du noeud de -180 à 180
        y.compute()
        orbite=y.orbit #Integer orbit number of epoch
        long=ep.degrees(y.sublong) #angle : minute : secondes
        long=float(repr(long))*180/ma.pi #-180 à 180
        lat=ep.degrees(y.sublat) #angle : minute : secondes
        lat=float(repr(lat))*180/ma.pi #-180 à 180
        elev=y.elevation #en m
        inclinaison=y.inc #en °
        anom_moy=ep.degrees(y._M) #angle : minute : secondes
        anom_moy=float(repr(anom_moy))*180/ma.pi #en °
        argument=y.ap #en °
        sql = "INSERT INTO satellites (idSatellite ,nomSatellite ,category ,orbite ,longitude ,latitude ,altitude ,inclinaison ,longitudeNoeud ,anomalieMoyenne ,semiMajorAxis ,semiMinorAxis ,arg ,source ,idUser, idPays) VALUES ( %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s)"
        param=(str(ids), str(x), str(category), str(orbite), str(long), str(lat), str(elev), str(inclinaison), str(RA), str(anom_moy), str(semiMajorAxis), str(semiMinorAxis), str(argument), 'celestrak',NULL,NULL)
        mycursor.execute(sql, param)
        DB_SERVER.commit()
        
        
        
        ids +=1
    

       
insert(last_30_days)
# insert(space_stations)
# insert(brightest)
# insert(active)
# insert(analyst)
# insert(cosmos_1408)
# insert(microsat_r)
# insert(fengyun_1c)
# insert(iridium_33_debris)
# insert(cosmos_2251_debris)
# insert(weather)
# insert(noaa)
# insert(goes)
# insert(resource)
# insert(sarsat)
# insert(disaster_monitoring)
# insert(tdrss)
# insert(argos)
# insert(planet)
# insert(spire)
# insert(geosynchronous)
# insert(gpz)
# insert(gpz_plus)
# insert(intelsat)
# insert(ses)
# insert(iridium)
# insert(iridium_next)
# insert(starlink)
# insert(oneweb)
# insert(orbcomm)
# insert(globalstar)
# insert(swarm)
# insert(amateur_radio)
# insert(experimental_comm)
# insert(other_comm)
# insert(satnogs)
# insert(gorizont)
# insert(raduga)
# insert(molniya)
# insert(gnss)
# insert(gps_ops)
# insert(glonass_ops)
# insert(galileo)
# insert(beidou)
# insert(sbas)
# insert(nnss)
# insert(russian_leo_navigation)
# insert(science)
# insert(geodetic)
# insert(engineering)
# insert(education)
# insert(military)
# insert(radar)
# insert(cubesat)
# insert(other)


close_bd(mycursor, DB_SERVER)
