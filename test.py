from geoloc import getLoc
from haversine import haversine

coordinates = {
    # latitude, longitude
    "Skogafoss": [63.532051, -19.511372],
    "Tianzi": [-33.714359, 150.311539],
    "Glowworm Caves": [-38.260630, 175.093730],
    "Kjeragbolten": [-33.714359, 150.311539],
    "Mount Fuji": [35.361709, 138.727363],
    "Masazir Lake": [40.509356, 49.770314],
    "Ha Long Bay": [21.337423, 107.142017],
    "The Dead Sea": [31.561094, 35.476548],
    "Tegalalang Rice Terrace": [-8.426753, 115.281162],
    "Reynisfjara Beach": [63.407344, -19.071735],
    "China's Stone Forest": [37.058915, 104.232844],
    "Marble Caves": [-46.658554, -72.628133],
    "Bioluminescent Beaches": [-0.616846, 73.093912],
    "The rugged Cliffs of Moher": [52.971846, -9.431139],
    "Isle of Skye": [57.291137, -6.221844],
    "Iguazu Falls": [-25.687796, -54.437931],
    "Tianmen Cave": [29.074153, 110.481484],
    "The Blyde River Canyon": [-24.590611, 30.812800],
    "Angel Falls": [5.970210, -62.536213]
}

city = getLoc("Tokyo")
closeNatureSites = []
for x, y in coordinates.items():
    dist = haversine(y[0], y[1], city[0], city[1])
    print(y[0] + y[1])
    #if distance is less than 2500km
    if dist < 4000:
        closeNatureSites.append(x)

#print(coordinates)
print(closeNatureSites)