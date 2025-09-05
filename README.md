# 🌦 Weather Forecast Web Application  

A full-stack **Flask web application** that fetches real-time weather and local time for any city using the **OpenWeatherMap API**. The app stores historical weather data in **MongoDB**, allowing users to revisit previous searches.  

![Weather App Preview](https://github.com/Srinu363/weather_report/blob/main/weather/static/light%20snow.jpg)  
*(Sample UI: replace with your own screenshot)*  

---

## 🚀 Features  

- 🌍 **Real-time Weather Data** – Fetches temperature, humidity, wind speed, and weather conditions for any city.  
- 🕒 **Local Time Conversion** – Calculates the city’s local time using timezone offset.  
- 🎨 **Dynamic UI Themes** – Background updates based on weather (clear sky, rain, snow, clouds, etc.).  
- 📦 **MongoDB Integration** – Stores search history and displays previous queries.  
- ⚠️ **Error Handling** – Custom pages for invalid cities and API errors.  

---

## 🛠️ Tech Stack  

- **Backend:** Python, Flask  
- **Database:** MongoDB  
- **APIs:** OpenWeatherMap API  
- **Frontend:** HTML, CSS (Jinja2 Templates)  
- **Libraries:** Requests, Datetime, PyMongo  

---

## 📂 Project Structure  

WeatherApp/
│── templates/
│ ├── input.html # User input page
│ ├── output.html # Weather results page
│ ├── previous.html # History page
│ ├── citynotfound.html # Error page
│
│── app.py # Main Flask application
│── requirements.txt # Dependencies
│── README.md # Documentation
