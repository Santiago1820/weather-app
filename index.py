import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

# Funcion get_weather
def get_weather(city):
    API_key = "931b35a51d2a7f2602095cc3ae080fd4"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)
    if res.status_code == 400:
        messagebox.showerror("Error", "Ciudad no encontrada")
        return None
    
    # Obtener nuestro JSON de nuestra api
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15  # 273.5 es farenhait a c
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    # obtener el icono por una url
    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)

# Definimos la variable search
def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    # Que va a pasar si se encuentra la ciudad
    icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{city}{country}")

    # obtener la imagen de la url
    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    # Actualizamos la imagen y la descripcion
    temperature_label.configure(text=f"Temperatura: {temperature:.2f}°C")
    description_label.configure(text=f"Descripción: {description}")

root = ttkbootstrap.Window(themename="morph")
root.title("Saniago - Weather App")
root.geometry("400x400")

#Diseño de barra
city_entry= ttkbootstrap.Entry(root, font="Helvetica, 18")
city_entry.pack(pady=10)

#Diseño barra boton buscar
search_button=ttkbootstrap.Button(root, text="Buscar", command=search, bootstyle="succesfull")
search_button.pack(pady=10)

#Estilo de la locacion
location_label= tk.Label(root, font="Helvetica, 25")
location_label.pack(pady=20)

#Estilo de el icono
icon_label = tk.Label(root)
icon_label.pack()

#Estilo de la temperatura
temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

#Estilo de la descripcion
description_label = tk.Label(root, font="Helvetica, 18")
description_label.pack()

root.mainloop()