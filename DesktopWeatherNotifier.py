﻿#importing modules
import time
from tkinter import *
from tkinter import messagebox as mb
import requests
from plyer import notification

#Function to get notification of weather report
def getNotification():
    cityName=place.get() #getting input of name of the place from user
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?" #base url from where we extract weather report
    try:
        # This is the complete url to get weather conditions of a city
        complete_url = baseUrl + "appid=" + "API_KEY" + "&q=" + cityName  
        response = requests.get(complete_url) #requesting for the the content of the url
        x = response.json() #converting it into json 
        y = x["main"] #getting the "main" key from the json object
 
        # getting the "temp" key of y
        temp = y["temp"]
        temp =(y["temp"]-273)*(9/5)+32 #converting temperature from kelvin to fahrenheit

        # storing the value of the "pressure" key of y
        pres = y["pressure"]

        # getting the value of the "humidity" key of y
        hum = y["humidity"]

        # storing the value of "weather" key in variable z
        z = x["weather"]

        # getting the corresponding "description"
        weather_desc = z[0]["description"]

        # combining the above values as a string 
        info = "Temperature = " + str(round(temp)) + "°F" +\
        "\n Atmospheric pressure = " + str(pres) +\
        "hPa" + "\n Humidity = " + str(hum) + "%" +\
        "\n Description: " + str(weather_desc)

        # showing the notification 
        notification.notify(
                    title = "Weather Report For:" + " " + cityName.title(),
                    message=info,

                    # displaying time
                    timeout=2)
        # waiting time
        time.sleep(7)
    
    except Exception as e:
        mb.showerror("Error",e)#show pop up message if any error occurred
        
# creating the window
wn = Tk()
wn.title("Weather Desktop Notifier")
wn.geometry("500x400")
wn.config(bg="azure")

# Heading label
Label(wn, text="Weather Desktop Notifier", font=("Courier", 15), fg="grey19",bg="azure").place(x=125,y=15)

# Getting the palce name 
Label(wn, text='Enter the Location:', font=("Courier", 13), fg="grey19", bg="azure").place(relx=0.05, rely=0.3)

place = StringVar(wn)
place_entry = Entry(wn, width=50, textvariable=place)
place_entry.place(relx=0.5, rely=0.3)

# Button to get notification
btn = Button(wn, text="Get Notification", font=7, fg="grey19",command=getNotification).place(relx=0.4, rely=0.75)
# run the window till the closed by user
wn.mainloop()
