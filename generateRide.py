import random
import folium
from geopy.distance import distance

START_LAT = <YourLatitude>
START_LON = <YourLongitude>

MAX_DISTANCE = 10
LOCATION_COUNT = 5

#Generate Tourtasks
content = open("tasks.txt","r").read().split("\n")
for i in range(0,6):
    index = random.randint(0,len(content) -1)
    print(content[random.randint(0,index)])
    del content[index]


#Generate start
m = folium.Map(location=[START_LAT, START_LON], zoom_start=12)
bearing = random.uniform(0, 360)
dist = random.uniform(1, 1)
origin = (START_LAT, START_LON)
destination = distance(kilometers=dist).destination(origin, bearing)
folium.Marker(
    [START_LAT, START_LON],
    popup="Start",
    icon=folium.Icon(color="green", icon="home")
).add_to(m)

#Generate destinations
for i in range(0,LOCATION_COUNT):
    bearing = random.uniform(0, 360)
    dist = random.uniform(1, MAX_DISTANCE)
    origin = (START_LAT, START_LON)

    destination = distance(kilometers=dist).destination(origin, bearing)

    folium.Marker(
        [destination.latitude, destination.longitude],
        popup=f"Random-{i} ({dist:.2f} km)",
        icon=folium.Icon(color="red", icon="flag")
    ).add_to(m)

    print("Destination:", destination.latitude, destination.longitude)




m.save("random_adventure_ride.html")
