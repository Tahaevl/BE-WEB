from asyncio.windows_events import NULL
from unicodedata import category
import ephem as ep
import math as ma
import mysql.connector

Gearth = 3.986004418*(10**14)

L=['TK-2', '1 52150U 22031A   22117.25510885  .00001670  00000+0  17634-3 0  9995', '2 52150  97.7981 290.3210 0014127 162.1534 198.0182 14.90542456  4294']
sat=ep.readtle(L[0],L[1],L[2])

print(sat)
# <ephem.EarthSatellite 'TK-2' at 0x000001C6A94F1730>

#ids = 1
#category = "{}".format(dic)
n = float(sat.n)*2*ma.pi/86400
semiMinorAxis = (n**2*Gearth)**(1/3)
e = sat.e
semiMajorAxis = semiMinorAxis*(1-e**2)**(1/2)
RA=sat.raan #ascension droite de 0° à 360°
if RA>180:
    RA-=360 #longitude de -180 à 180
sat.compute()

orbite=sat.orbit # Integer orbit number of epoch
print(orbite)
# 429

long=ep.degrees(sat.sublong) # -180 à 180
print(float(repr(long))*180/ma.pi)
#-24:58:30.5

lat=ep.degrees(sat.sublat) # -180 à 180
print(float(repr(lat))*180/ma.pi)
#-65:15:32.1

elev=sat.elevation #en m
print(elev)
#630729.625 non verifiable

inclinaison=sat.inc #en °
print(inclinaison)
#97.79810333251953 bon

long_noeud=RA # -180 à 180
print(long_noeud)
#-69.67898559570312 bon sauf que de 0° à 360°

anom_moy=ep.degrees(sat._M) #en °
print(float(repr(anom_moy))*180/ma.pi)
#198:01:05.5

print(semiMajorAxis)
#776.5792992505485

print(semiMinorAxis)
#776.5800741696802

argument=sat.ap #en °
print(argument)
#162.1533966064453 bon

#revoir car problème pour la conversion degrees et elevation