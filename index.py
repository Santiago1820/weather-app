import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

#Funcion get_weather
def get_weather(city):
    API_key= "931b35a51d2a7f2602095cc3ae080fd4"
    url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)
    if res.status_code == 400:
        messagebox.showerror("Error", "Ciudad no encontrada")
        return None
    
#Obtener nuestro JSON de nuestra api
weather = res.JSON()
icon_id = weather['weather'][0]['icon']
temperature = weather['main']['temp'] - 273.15 #273.5 es farenhait a c

#Definimos la variable search
def search():
    city = city_etry.get()
    result = get_weather(city)
    if result is None:
        return

root = ttkbootstrap.Window(themename="morph")
root.title("Saniago - Weather App")
root.geometry("400x400")

#Diseño de barra
city_etry= ttkbootstrap.Entry(root, font="Helvetica, 18")
city_etry.pack(pady=10)

#Diseño barra boton buscar
search_button=ttkbootstrap.Button(root, text="Buscar", command=search, bootstyle="succesfull")
search_button.pack(pady=10)

#Comentario
location_label= tk.Label(root, font="Helvetica, 25")
location_label.pack(pady=20)

#Comentario
icon_label = tk.Label(root)
icon_label.pack()

#Comentario
temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

#Comentario
description_label = tk.Label(root, font="Helvetica, 18")
description_label.pack()

root.mainloop()