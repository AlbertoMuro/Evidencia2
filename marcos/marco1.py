import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt

def marco1():
    texto1 = sg.Text("Análisis AIRBNB", key='TEXT1', size=(920, 1), background_color='#ff375b', font=("Helvetica", 30), justification='center', border_width=10)
    
    inner_frame_layout = [
        [sg.Text("Ingresa la contraseña", background_color="#ff375b", pad= (0,0), justification = "center")],
        [sg.Input(key='PASSWORD', size=(15, 1), justification = "center")],
        [sg.Button("Iniciar Sesion", key='LOGIN', size=(15, 1), button_color=("#ffffff", '#ff375b'), font=("Helvetica", 15), border_width=10)]
    ]
    inner_frame = sg.Frame("", inner_frame_layout, background_color='#ff375b', pad = (0,0))

    layout = [
        [texto1],
        [sg.Column([[inner_frame]], justification='center', pad= (0,0))],  # Centrar el marco interno
        [sg.Column([[sg.Image(filename='img/airbnb.png', size=(200, 200), pad= (0,0))]], justification='center')]  # Centrar la imagen
    ]
    frame = sg.Frame('Varios Elementos', layout, key='FRAME1', size=(960, 540), background_color='#fff')

    return frame