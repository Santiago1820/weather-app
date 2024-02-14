# Importamos las librerias que vamos a utilizar
# Tkinter e suna libreria para poder ejecutar ventanas nativas en nuestro codigo
import tkinter as tk

# Importamos requests para poder hacer una llamada a la pagina www.openweathermap.org la cual nos dará los datos que vmos a buscar
import requests

# De la libreria tkinter vamos a importar la función de messagebox para poder mostrar un mensaje en caso de que no se muestre nuestra ciudad buscada
from tkinter import messagebox

# Importamos la libreria PIL y utilizamos las funciones Image e ImageTk para poder mostrarr las imagenes que extraemos de nuestra api
from PIL import Image, ImageTk

# Importamos la libreria tkbootsrap para poder darle un diseño pre-hcho y ahorrarnos ddarle diseño a nuestra interfaz
import ttkbootstrap

# Funcion get_weather
def get_weather(city):
    #Establecemos nuestra api key la cual nos dara la posibilida de llamar a la pagina y que nos resonda el servidor con los dtos
    API_key = "931b35a51d2a7f2602095cc3ae080fd4"
    # establecemos la url a la cual le soliccitaremos los daros, en estos casos le pasaremos los parametros de la ciudad y nuestra api, la cual nos devolvera la temperatura y una descripcion de ella
    # El parametro q= es para poder buscar la ciudad, el parametro lang= es para poder establecer el lenguaje el cual nos dirá la descripción, el parametro appid= es para pasar nuestra api y por ultimo el parametro units= es para establecer la temperatura en grados centigrados, podemos ver más informacion en la página de openweathermap.org
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&lang=es&appid={API_key}&units=metric"
    # De nuestra url vamos a usar la libreria requets para hacer el llamado a nuestro servidor y los resultados lo guardaremos en la variable res
    res = requests.get(url)
    # Hacemos una prueba logica la cual si no encontramos o el servidor nos contesta como invalido mostramos un mensaje de error 
    if res.status_code == 400:
        messagebox.showerror("Error", "Ciudad no encontrada")
        return None
    
    # Obtener nuestro JSON de nuestra api
    weather = res.json()
    # Del JSON obtenemos el icono la cual la página nos arrojara, seguido de su temperatura, luego la transformaremos a grados C ya que nos la arroja en F
    #icon_id lo utilizamos para obtener nuestra iagen
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp']
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    # obtener el icono por una url
    # con la función icon_url sabremos que imagen nos va a mostrar pasandole el parametro de icon_id
    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    # retornaremos nuestra imagen, nuestra temoperatura, descripcion, ciudad y el pais.
    return (icon_url, temperature, description, city, country)

# Definimos la variable de buscar la cual dara el motor de busqueda de ciudades de nuestro sistema
def search():
    # Ciudad va a ser igual a la entrada de ciudad
    city = city_entry.get()
    # Resulado va a ser igual al resultado de la ciudad que ingresamos
    result = get_weather(city)
    if result is None:
        return
    # Que va a pasar si se encuentra la ciudad
    icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{city}{country}")

    # Le damos un diseño a la imagen de nuestra ciudad
    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    # Actualizamos la imagen y la descripcion
    temperature_label.configure(text=f"Temperatura: {temperature:.2f}°C")
    description_label.configure(text=f"Descripción: {description}")

root = ttkbootstrap.Window(themename="darkly")
root.title("Saniago - Weather App")
root.geometry("500x600")

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

# Por ultimo mostraremos nuestra ventana que creamos al inicio con la aplicación tkinter
root.mainloop()