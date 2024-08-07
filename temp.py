import firebase_admin
from firebase_admin import credentials, db

# Path to the service account key JSON file
cred_2 = credentials.Certificate(
    'routemappothole-firebase-adminsdk-han37-9bfaad953a.json')

# Initialize the app with a custom auth variable, limiting the server's access
firebase_app2 = firebase_admin.initialize_app(cred_2, {
    'databaseURL': 'https://routemappothole-default-rtdb.firebaseio.com/',
}, name='second-db')


ref2 = db.reference('/', app=firebase_app2)
data2 = ref2.get()

arr21 = []  # route latitude
arr22 = []  # route longitude

y = 0
for d in data2:
    y = y+1
for i in range(y):
    var = 'test' + str(i)
    lati2 = data2[var]['lat']
    arr21.append(lati)
    long2 = data2[var]['lon']
    arr22.append(long)
# new_user_ref = ref.push({
#     'laptop': 'johnhp22',
#     'name': 'John'
# })

# print(data['test0']['Lat'])
# query = ref.order_by_child("timestamp")
# results = query.get()
# print(data)
# arr1 = []
# arr2 = []
# arr3 = []

# x = 0
# for d in data:
#     x = x+1

# for i in range(x):
#     var = 'test' + str(i)
#     lati = data[var]['Lat']
#     arr1.append(lati)
#     long = data[var]['Lon']
#     arr2.append(long)
#     string = data[var]['String']
#     arr3.append(string)

# link = arr3[x-1]

# for i in arr3:
#     print(i)

# print(x)
# print(link)

# print(i)
# print(results)
# print("xxcc")

# import polyline

# # Define a list of latitude and longitude points
# points = [
#     (37.772323, -122.214897),
#     (21.291982, -157.821856),
#     (-18.142599, 178.431),
#     (-27.46758, 153.027892),
# ]

# # Encode the list of points into a polyline
# polyline_str = polyline.encode(points)

# # Output the polyline string
# print(polyline_str)

# import googlemaps

# # Set up Google Maps API key
# gmaps = googlemaps.Client(key='AIzaSyD3cImlKOCldEZPJfvIBXOKeSsAjA5V200')

# # Define list of coordinates to snap
# coordinates = [(40.714224, -73.961452), (40.713926, -73.962028), (40.713492, -73.963297)]

# # Snap coordinates to nearest road
# snapped_points = gmaps.snap_to_roads(coordinates)['snappedPoints']

# # Extract latitude and longitude of snapped points
# snapped_coordinates = []
# for point in snapped_points:
#     lat = point['location']['latitude']
#     lng = point['location']['longitude']
#     snapped_coordinates.append((lat, lng))

# # Display snapped coordinates
# print(snapped_coordinates)
