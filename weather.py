import streamlit as st
import requests

# OpenWeather API Key
API_KEY = "ec36d08991973dda2a899959796c3764"  # Replace with your actual OpenWeather API key

# Function to get weather data
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# Streamlit UI
st.title("🌦 OpenWeather App")

# User Input
city = st.text_input("Enter City Name", "Mumbai")

if st.button("Get Weather"):
    weather_data = get_weather(city)
    
    if weather_data:
        st.subheader(f"Weather in {city}")
        st.write(f"🌡 Temperature: {weather_data['main']['temp']}°C")
        st.write(f"🌬 Wind Speed: {weather_data['wind']['speed']} m/s")
        st.write(f"🌤 Weather: {weather_data['weather'][0]['description'].title()}")
    else:
        st.error("❌ City not found. Please enter a valid city name.")
