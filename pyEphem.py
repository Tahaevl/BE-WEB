from asyncio.windows_events import NULL
from unicodedata import category
import ephem as ep
import math
import mysql.connector

mydb = mysql.connector.connect(user="root", password="",host="localhost",port=3306,database="ienac21_elhassouni_gonzalez_houze_locatelli ",raise_on_warnings=True)
Gearth = 3.986004418*(10**14)


def tle(file):
    f = open(file,'r')
    L = f.readlines()
    n = len(L)

    for i in range(0,n//3,3):
        sky = {}
    
        sky[L[i]]=ep.readtle(L[i],L[i+1],L[i+2])
    f.close()
    return sky

# Special-Interest Satellites

last_30_days=tle("C:\\Users\\Clément\\OneDrive\\Bureau\\Cours WEB\\TLE_satellites\\last-30-days.txt")
space_stations=tle("C:\\Users\\Clément\\OneDrive\\Bureau\\Cours WEB\\TLE_satellites\\space-stations.txt")
brightest=tle("C:\\Users\\Clément\\OneDrive\\Bureau\\Cours WEB\\TLE_satellites\\visual.txt")
active=tle("C:\\Users\\Clément\\OneDrive\\Bureau\\Cours WEB\\TLE_satellites\\active.txt")
analyst=tle("C:\\Users\\Clément\\OneDrive\\Bureau\\Cours WEB\\TLE_satellites\\analyst")
cosmos_1408=tle("C:\\Users\\Clément\\OneDrive\\Bureau\\Cours WEB\\TLE_satellites\\1982-092.txt")
microsat_r=tle("C:\\Users\\Clément\\OneDrive\\Bureau\\Cours WEB\\TLE_satellites\\2019-006.txt")
fengyun_1c=tle("C:\\Users\\Clément\\OneDrive\\Bureau\\Cours WEB\\TLE_satellites\\1999-025.txt")
iridium_33_debris=tle("C:\\Users\\Clément\\OneDrive\\Bureau\\Cours WEB\\TLE_satellites\\iridium-33-debris")
cosmos_2251_debris=tle("C:\\Users\\Clément\\OneDrive\\Bureau\\Cours WEB\\TLE_satellites\\cosmos-2251-debris")

# Weather and Earth Ressources Satellites
weather=tle("C:\\Users\\Clément\\OneDrive\\Bureau\\Cours WEB\\TLE_satellites\\weather.txt")
noaa=tle("C:\\Users\\Clément\\OneDrive\\Bureau\\Cours WEB\\TLE_satellites\\noaa.txt")
goes=tle("C:\\Users\\Clément\\OneDrive\\Bureau\\Cours WEB\\TLE_satellites\\goes.txt")
resource=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/resource.txt")
sarsat=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/sarsat.txt")
disaster_monitoring=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/dmc.txt")
tdrss=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/tdrss.txt")
argos=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/argos.txt")
planet=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/planet.txt")
spire=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/spire.txt")

#Communications Satellites

geosynchronous=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/geo.txt")
gpz=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/gpz.txt")
gpz_plus=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/gpz-plus.txt")
intelsat=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/intelsat.txt")
ses=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/ses.txt")
iridium=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/iridium.txt")
iridium_next=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/iridium-next.txt")
starlink=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/starlink.txt")
oneweb=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/oneweb.txt")
orbcomm=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/orbcomm.txt")
globalstar=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/globalstar.txt")
swarm=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/swarm.txt")
amateur_radio=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/amateur.txt")
experimental_comm=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/x-comm.txt")
other_comm=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/other-comm.txt")
satnogs=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/satnogs.txt")
gorizont=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/gorizont.txt")
raduga=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/raduga.txt")
molniya=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/molniya.txt")

# Navigation Satellites

gnss=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/gnss.txt")
gps_ops=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/gps-ops.txt")
glonass_ops=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/glo-ops.txt")
galileo=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/galileo.txt")
beidou=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/beidou.txt")
sbas=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/sbas.txt")
nnss=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/nnss.txt")
russian_leo_navigation=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/musson.txt")

# Scientific Satellites

science=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/science.txt")
geodetic=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/geodetic.txt")
engineering=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/engineering.txt")
education=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/education.txt")

#Miscellaneous Satellites

military=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/military.txt")
radar=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/radar.txt")
cubesat=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/cubesat.txt")
other=tle("C:/Users/Clément/OneDrive/Bureau/Cours WEB/TLE_satellites/other.txt")
 

def insert(dic):
    for x,y in dic.items() :
        ids = 1
        category = "{}".format(dic)
        n = float(y.n)*2*math.pi/86400
        semiMinorAxis = (n**2*Gearth)**(1/3)
        e = y.e
        semiMajorAxis = semiMinorAxis*(1-e**2)**(1/2)
        mydb.execute("INSERT INTO 'satellites' (idSatelitte ,nomSatelitte ,category ,orbite ,longitude ,latitude ,altitude ,inclinaison ,longitudeNoeud ,anomalieMoyenne ,semiMajorAxis ,semiMinorAxis ,arg ,source ,idUser, idPays) VALUES (:idSatelitte ,:nomSatelitte ,:category ,:orbite ,:longitude ,:latitude ,:altitude ,:inclinaison ,:longitudeNoeud ,:anomalieMoyenne ,:semiMajorAxis ,:semiMinorAxis ,:arg ,:source ,:idUser, :idPays)", [ids,x,category,y.orbit,y.lon,y.lat,y.elevation,y.inc,y._Om,y._M, semiMajorAxis,semiMinorAxis, y.ap, 'celestrak',NULL,NULL ])
        ids +=1
        
insert(last_30_days)
insert(space_stations)
insert(brightest)
insert(active)
insert(analyst)
insert(cosmos_1408)
insert(microsat_r)
insert(fengyun_1c)
insert(iridium_33_debris)
insert(cosmos_2251_debris)
insert(weather)
insert(noaa)
insert(goes)
insert(resource)
insert(sarsat)
insert(disaster_monitoring)
insert(tdrss)
insert(argos)
insert(planet)
insert(spire)
insert(geosynchronous)
insert(gpz)
insert(gpz_plus)
insert(intelsat)
insert(ses)
insert(iridium)
insert(iridium_next)
insert(starlink)
insert(oneweb)
insert(orbcomm)
insert(globalstar)
insert(swarm)
insert(amateur_radio)
insert(experimental_comm)
insert(other_comm)
insert(satnogs)
insert(gorizont)
insert(raduga)
insert(molniya)
insert(gnss)
insert(gps_ops)
insert(glonass_ops)
insert(galileo)
insert(beidou)
insert(sbas)
insert(nnss)
insert(russian_leo_navigation)
insert(science)
insert(geodetic)
insert(engineering)
insert(education)
insert(military)
insert(radar)
insert(cubesat)
insert(other)





