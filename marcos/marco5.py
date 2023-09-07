import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt

def marco5():
    opciones1 = ("Tasa de respuesta del anfitrión", "Tasa de aceptación del anfitrión", "Capacidad de la propiedad", "Precio", "Puntuación rating", "Puntuación precisión", "Puntuación limpieza", "Puntuación check in", "Puntuación comunicación host", "Puntuación ubicación", "Puntuación valor de la propiedad", "Mínimo de noches", "Máximo de noches", "Reviews por mes")
    combo1 = sg.Combo(opciones1, key='DESCRIPCION', default_value='Análisis Estadísticos', size=(20, 4), text_color='fff', font=('Helvetica', 14)) 
    texto2 = sg.Text("Análisis de Datos", key='TEXT2', size=(960, 1), background_color='#ff375b', font=('Helvetica', 30), justification='center', border_width=10)
    espacio_blanco1 = sg.Text("", size=(40, 1), background_color="#fff")
    imagen7 = sg.Image(filename = "img/estadisticos.png")
    texto7 = sg.Text("Análisis Airbnb", key='TEXT7', size=(30, 1), background_color = "#fff", text_color = "#ff375b", font=("Helvetica", 20), justification='left', border_width=10)
    espacio_blanco2 = sg.Text("", size=(40, 2), background_color="#fff")
    imagen2 = sg.Image(filename='img/flecha.png', size=(60,60), pad= (0,0))
    boton1 = sg.Button("Regresar", key = "REGRESAR", size=(15, 1), button_color=('#ff375b', "#ffffff"), font=("Helvetica", 20), border_width=10)
    boton2 = sg.Button("Enviar", key='OPCION', size=(10, 1), button_color=("#ffffff", '#ff375b'), font=("Helvetica", 10), border_width=10)


    layout = [[texto2],
              [combo1, boton2],
              [espacio_blanco1],
              [imagen7],
              [espacio_blanco2],
              [texto7, imagen2, boton1]
              ]

    # Alinear horizontalmente el contenido dentro del marco
    frame = sg.Frame("", layout, key='FRAME3', size=(960, 540), background_color='#fff', element_justification='c')

    return frame