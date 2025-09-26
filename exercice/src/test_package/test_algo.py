import math



def dms_to_radians (degrees, minutes, seconds, direction ="W") ->float :
    dd = (degrees + (minutes/60) + (seconds/3600))
    coef = -1 if direction =="W" or direction == "S" else 1
    return  math.radians( dd ) * coef


def distance(origine, destination):

   # Usage de la formule de haversine
    latitude = origine["latitude"]
    origine_latitude = dms_to_radians(latitude["degrees"], latitude["minutes"], latitude["seconds"], "W")
    print("origine_latitude", origine_latitude)

    longitude = origine["longitude"]
    origine_longitude = dms_to_radians(longitude["degrees"], longitude["minutes"], longitude["seconds"], "N")
    print("origine_longitude", origine_longitude)

    latitude = destination["latitude"]
    destination_latitude = dms_to_radians(latitude["degrees"], latitude["minutes"], latitude["seconds"], "W")
    print("destination_latitude", destination_latitude)

    longitude = destination["longitude"]
    destination_longitude = dms_to_radians(longitude["degrees"], longitude["minutes"], longitude["seconds"], "N")
    print("destination_longitude", destination_longitude)

    delta_latitude = destination_latitude - origine_latitude
    print("delta_latitude", delta_latitude)

    delta_longitude = destination_longitude - origine_longitude
    print("delta_longitude", delta_longitude)

    a = math.sin(delta_latitude/2)**2 + math.cos(origine_latitude)*math.cos(destination_latitude)*math.sin(delta_longitude/2)**2
    print("a ",a)
    c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
    print("c ",c)
    dist = 6371 * c
    print("dist ", dist)
    return dist

if __name__ == '__main__':
    # 34°45'21.8"N, 120°37'34.8"W
    # 43°44'41.7"N 96°49'37.4"W

    origine = { "latitude": {"degrees" : 34, "minutes" : 45, "seconds" : 21.8},
                "longitude": {"degrees" : 120, "minutes" : 37, "seconds" : 34.8}}

    destination = {"latitude": {"degrees" : 43, "minutes" : 44, "seconds" : 41.7},
                   "longitude": {"degrees" : 96, "minutes" : 49, "seconds" : 37.4}}

    print(" >>>  La distance devrait être autour de 2260 est de "  + str(distance(origine,destination)))
"""
[Debug] origine_latitude : -0.6066076044505114
[Debug] origine_longitude : 2.1053266812748532
[Debug] destination_latitude : -0.7634894331481084
[Debug] destination_longitude : 0.7634894331481084
[Debug] delta_latitude : -0.15688182869759693
[Debug] delta_latitude : -0.15688182869759693
[Debug] a : 0.23555311451699087
[Debug] c : 1.0134997494484685
"""
