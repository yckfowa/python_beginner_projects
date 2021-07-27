from tkinter import *
from tkinter import messagebox
from tkmacosx import Button
import requests

BLUE ='#D4F1F4'
MINT = '#E7F2F8'

def get_weather(city):

    api_key = "c0a8f7ba68ddf32588713508e1ad1b35"
    url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&cnt=3&APPID=%s' % (city, api_key)

    result = requests.get(url)
    if result:
        weather_data = result.json()
        #(City, Country, max_temp_celsius,min_temp_celsius,icon, weather)
        city = weather_data['name']
        country = weather_data['sys']['country']
        max_temp_celsius = weather_data['main']['temp_max'] - 273.15
        min_temp_celsius = weather_data['main']['temp_min'] - 273.15
        icon = weather_data['weather'][0]['icon']
        temp = weather_data['main']['temp'] - 273.15
        weather = weather_data['weather'][0]['main']
        final_data = (city, country, max_temp_celsius, min_temp_celsius,icon, weather, temp)
        return final_data


def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather: 
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        img['bitmap'] = 'weather_icons/{}.png'.format(weather[4])
        temp_lbl['text'] = 'Highest: {:.1f}°C & Lowerest: {:.1f}°C'.format(weather[2],weather[3])
        weather_lbl['text'] = 'Currently: {:.1f}°C'.format(weather[6])+' & '+ weather[5]
    else:
        messagebox.showerror("Error","City does not exist")


win = Tk()
win.title('Weather App')
win.geometry("280x300")
win.config(bg=BLUE)

city_text = StringVar()
city_entry = Entry(win, textvariable=city_text, justify='center',width=10)
city_entry.pack(padx= 50, pady= 20)

search_btn = Button(win, text='Search', bg=MINT,command=search)
search_btn.pack()

location_lbl = Label(win, text="",bg=BLUE, font=('bold',20))
location_lbl.pack()

img = Label(win, bitmap="",bg=BLUE)
img.pack()

temp_lbl = Label(win, text="",bg=BLUE)
temp_lbl.pack()

weather_lbl = Label(win, text='',bg=BLUE)
weather_lbl.pack()

win.mainloop()