from flask import Flask, request, render_template
from geopy.geocoders import Nominatim
import firebase_admin
import requests

from firebase_admin import credentials, db

app = Flask(__name__)

geolocator = Nominatim(user_agent="road_name_finder")

cred_1 = credentials.Certificate(
    'pothole-image-db-firebase-adminsdk-dkjle-4712d586c9.json')

# Initialize the app with a custom auth variable, limiting the server's access
firebase_app1 = firebase_admin.initialize_app(cred_1, {
    'databaseURL': 'https://pothole-image-db-default-rtdb.firebaseio.com/',
})

cred_2 = credentials.Certificate(
    'routemappothole-firebase-adminsdk-han37-9bfaad953a.json')

# Initialize the app with a custom auth variable, limiting the server's access
firebase_app2 = firebase_admin.initialize_app(cred_2, {
    'databaseURL': 'https://routemappothole-default-rtdb.firebaseio.com/',
}, name='second-db')


@app.route('/')
def home():
    # ref1 = db.reference('/', app=firebase_app1)
    # data = ref1.get()
    # x = 0
    # for d in data:
    #     x = x+1

    # for i in range(x):
    #     var = 'test' + str(i)
    #     lati = data[var]['Lat']
    #     long = data[var]['Lon']

    # location = geolocator.reverse(str(lati)+","+str(long))
    # location = "hello"
    #     return render_template("index.html",lati = lati, long = long, location = location, all = all, length = length)
    # """

    # ref = db.reference('/')
    # data = ref.get()

    return render_template("index.html")


@app.route('/main')
def maps():
    ref1 = db.reference('/', app=firebase_app1)
    data = ref1.get()
    x = 0
    for d in data:
        x = x+1

    for i in range(x):
        var = 'test' + str(i)
        lati = data[var]['Lat']
        long = data[var]['Lon']

    location = geolocator.reverse(f"{lati}, {long}")
    # location = geolocator.reverse(str(lati)+","+str(long))

    # return render_template("maps.html", lati=lati, long=long)#, location=location, all=all, length=length)
    arr1 = []  # pothole lati
    arr2 = []  # pothole longitude
    arr3 = []  # pothole picture location

    x = 0
    for d in data:
        x = x+1

    for i in range(x):
        var = 'test' + str(i)
        lati = data[var]['Lat']
        arr1.append(lati)
        long = data[var]['Lon']
        arr2.append(long)
        string = data[var]['String']
        arr3.append(string)

    link = arr3[x-1]

    # for route_map
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
        arr21.append(lati2)
        long2 = data2[var]['lon']
        arr22.append(long2)

    return render_template("maps.html", lati=lati, long=long, arr1=arr1, arr2=arr2, arr3=arr3, link=link, location=location, lati2=lati2, long2=long2, route_arr1=arr21, route_arr2=arr22)


@app.route('/streetView')
def street():
    ref1 = db.reference('/', app=firebase_app1)
    data = ref1.get()
    x = 0
    for d in data:
        x = x+1

    for i in range(x):
        var = 'test' + str(i)
        lati = data[var]['Lat']
        long = data[var]['Lon']
    return render_template("street/street.html", lati=lati, long=long)


if __name__ == "__main__":
    app.run(debug=True)
