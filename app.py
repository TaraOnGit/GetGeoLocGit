from flask import Flask, render_template, request
from db import Database
from location import Location
from weather_info import WeatherInfo

app = Flask(__name__)
dbo = Database()
loc = Location()
w = WeatherInfo()


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/perform_login', methods=['post'])
def perform_login():
    email = request.form.get('Email')
    password = request.form.get('Password')

    response = dbo.search(email,password)
    print(response)

    if response :
        return render_template('profile.html')
    else :
        return render_template('login.html', message = 'Invalid User Details. Try Again')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name = request.form.get('Name')
    email = request.form.get('Email')
    password = request.form.get('Password')

    response = dbo.insert(name, email, password)

    if response == 0 :
        return render_template('login.html', message='Registered Successfully. Login to proceed')
    else:
        return render_template('register.html', message='User Already Exists')

@app.route('/address')
def address():
    return render_template('address.html')

@app.route('/getLatLong',methods=['post'])
def getLatLong():
    address = request.form.get('Address')

    lat,long = loc.getLatLong(address)
    dic = {'Latitude' : lat, 'Longitude' : long}
    return dic

@app.route('/weather')
def weather():
    return render_template('weather_gui.html')

@app.route('/getWeatherInfo',methods=['post'])
def getWeatherInfo():
    lat = request.form.get('Latitude')
    long = request.form.get('Longitude')

    response = w.weatherInfo(lat, long)
    return dict(response)



app.run(debug=True)



