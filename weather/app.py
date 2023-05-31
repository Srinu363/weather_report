from flask import Flask, request, render_template
from pymongo import MongoClient
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['srinu']
collection = db['weather']

# API key to access OpenWeatherMap API
api_key = 'f77b28787c5b189e0ba8d333a6ac8205'

@app.route('/')
def home():
    # Render the input.html template when the user navigates to the home page
    return render_template('input.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    # Get the name of the city that the user entered in the form
    city = request.form['city']
    
    # Construct the URL for the OpenWeatherMap API request using the city name and API key
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    
    # Send the HTTP GET request to the OpenWeatherMap API and get the response
    weather_response = requests.get(weather_url)

    if weather_response.status_code ==200: # if the OpenWeatherMap API request was successful
        # Extract the relevant weather data from the JSON response
        weather_data = weather_response.json()
        weather = weather_data['weather'][0]['description']
        temp = round(weather_data['main']['temp'] - 273.15, 2)  # Convert to Celsius
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        # Construct the URL for the time zone API request using the city name and API key
        timezone_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        # Send the HTTP GET request to the time zone API and get the response
        timezone_response = requests.get(timezone_url)

        if timezone_response.status_code == 200: # if the time zone API request was successful
            # Extract the relevant time zone data from the JSON response
            timezone_data = timezone_response.json()
            timezone_offset = timezone_data['timezone']
            
            # Get the current UTC time
            current_time_utc = datetime.utcnow()

            # Add the timezone offset to the current UTC time to get the local time in the city
            local_time = current_time_utc + timedelta(seconds=timezone_offset)

            # Save the weather data to the MongoDB database
            weather_doc = {
                'city': city,
                'weather': weather,
                'temp': temp,
                'humidity': humidity,
                'wind_speed': wind_speed,
                'local_time': local_time
            }
            collection.insert_one(weather_doc)

            # Render the output.html template with the weather and time data to display to the user
            return render_template('output.html', city=city, weather=weather, temp=temp, humidity=humidity, wind_speed=wind_speed, local_time=local_time)
        else:
            # If the time zone API request was unsuccessful, display an error message to the user
            return "Time zone data not found."
    else:
        # If the OpenWeatherMap API request was unsuccessful, display an error message to the user
        return render_template('citynotfound.html')


if __name__ == '__main__':
    # Start the Flask application in debug mode
    app.run(debug=True)

