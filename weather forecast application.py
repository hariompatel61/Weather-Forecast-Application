import tkinter as tk
from tkinter import messagebox
import requests

def get_weather_data(location):
    api_key = "6b4307aa4192788fa1f619c2fdbe694c"  # Replace this with your actual API key from OpenWeatherMap.
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # You can change this to "imperial" for Fahrenheit.
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def show_weather():
    location = location_entry.get()
    weather_data = get_weather_data(location)
    
    if weather_data:
        city_name = f"City: {weather_data['name']}"
        temperature = f"Temperature: {weather_data['main']['temp']}°C"
        humidity = f"Humidity: {weather_data['main']['humidity']}%"
        wind_speed = f"Wind Speed: {weather_data['wind']['speed']} m/s"
        description = f"Description: {weather_data['weather'][0]['description'].capitalize()}"
        
        weather_info = "\n".join([city_name, temperature, humidity, wind_speed, description])
        messagebox.showinfo("Weather Information", weather_info)
    else:
        messagebox.showerror("Error", "Weather data not available.")

# Create the main window
root = tk.Tk()
root.title("Weather Forecast Application")
root.geometry("400x300")  # Set the window size

# Define colors
background_color = "#f0f0f0"
button_color = "#007BFF"
button_hover_color = "#0056b3"
label_color = "#333"

# Set window background color
root.config(bg=background_color)

# Create widgets with color styling
location_label = tk.Label(root, text="Enter the name of a city or a zip code:", bg=background_color, fg=label_color, font=("Arial", 16, "bold"))
location_entry = tk.Entry(root, font=("Arial", 14))
get_weather_button = tk.Button(root, text="Get Weather", bg=button_color, fg="white", activebackground=button_hover_color, font=("Arial", 14), command=show_weather)

# Layout widgets using grid
location_label.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
location_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
get_weather_button.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

# Additional customization
location_entry.focus()  # Set focus on the entry field by default

# Run the main event loop
root.mainloop()
