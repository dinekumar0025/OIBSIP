from tkinter import *
from tkinter import messagebox
import requests

API_KEY = "a558ff252885b9011613039e6c25af09"

def get_weather():

    city = city_entry.get()

    if city == "":
        messagebox.showerror("Error", "Please enter city name")
        return

    try:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        data = response.json()

        if str(data["cod"]) != "200":
            messagebox.showerror("Error", "City not found")
            return

        # WEATHER DETAILS
        
        city_name = data["name"]
        country = data["sys"]["country"]

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]

        weather = data["weather"][0]["description"]

        wind = data["wind"]["speed"]

        result_label.config(
            text=f"""
City : {city_name}, {country}

Temperature : {temp} °C

Humidity : {humidity} %

Pressure : {pressure} hPa

Wind Speed : {wind} m/s

Condition : {weather}
"""
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))

# CLEAR FUNCTION

def clear_data():

    city_entry.delete(0, END)

    result_label.config(text="")

# MAIN WINDOW

root = Tk()

root.title("Weather App")

root.geometry("500x500")

root.config(bg="skyblue")

root.resizable(False, False)

title_label = Label(
    root,
    text="WEATHER APP",
    font=("Arial", 24, "bold"),
    bg="skyblue",
    fg="black"
)

title_label.pack(pady=20)
 

city_entry = Entry(
    root,
    font=("Arial", 18),
    width=25
)

city_entry.pack(pady=20)

# SEARCH BUTTON
search_button = Button(
    root,
    text="Get Weather",
    font=("Arial", 14, "bold"),
    bg="green",
    fg="white",
    command=get_weather
)

search_button.pack(pady=10)

# CLEAR BUTTON
clear_button = Button(
    root,
    text="Clear",
    font=("Arial", 14, "bold"),
    bg="red",
    fg="white",
    command=clear_data
)

clear_button.pack(pady=10)

result_label = Label(
    root,
    text="",
    font=("Arial", 15),
    bg="skyblue",
    justify=LEFT
)

result_label.pack(pady=30)
root.mainloop()
