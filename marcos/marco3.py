import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt

def marco3():
    texto2 = sg.Text("Gráficos", key='TEXT2', size=(920, 1), background_color='#ff375b', font=("Helvetica", 30), justification='center', border_width=10)
    texto3 = sg.Button("Gráfico 1", key='BUTTON3', size=(40, 5), button_color=("#ffffff", '#ff375b'), font=("Helvetica", 15), border_width=10)
    texto4 = sg.Button("Gráfico 2", key='BUTTON4', size=(40, 5), button_color=("#ffffff", '#ff375b'), font=("Helvetica", 15), border_width=10)
    texto5 = sg.Button("Gráfico 3", key='BUTTON5', size=(40, 5), button_color=("#ffffff", '#ff375b'), font=("Helvetica", 15), border_width=10)
    texto6 = sg.Button("Gráfico 4", key='BUTTON6', size=(40, 5), button_color=("#ffffff", '#ff375b'), font=("Helvetica", 15), border_width=10)
    texto7 = sg.Text("Análisis Airbnb", key='TEXT7', size=(30, 1), background_color = "#fff", text_color = "#ff375b", font=("Helvetica", 20), justification='left', border_width=10)
    espacio_blanco1 = sg.Text("", size=(40, 1), background_color="#fff")
    espacio_blanco2 = sg.Text("", size=(40, 1), background_color="#fff")
    imagen2 = sg.Image(filename='img/flecha.png', size=(60,60), pad= (0,0))
    boton1 = sg.Button("Regresar", key = "REGRESAR", size=(15, 1), button_color=('#ff375b', "#ffffff"), font=("Helvetica", 20), border_width=10)

    layout = [[texto2],
              [espacio_blanco1],
              [texto3, texto4],
              [texto5, texto6],
              [espacio_blanco2],
              [texto7, imagen2, boton1]
              ]

    # Alinear horizontalmente el contenido dentro del marco
    frame = sg.Frame("", layout, key='FRAME3', size=(960, 540), background_color='#fff', element_justification='c')

    return frame