import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt

def marco1():
    texto1 = sg.Text("Análisis AIRBNB", key='TEXT1', size=(920, 1), background_color='#ff375b', font=("Helvetica", 30), justification='center', border_width=10)
    
    inner_frame_layout = [
        [sg.Text("Ingresa la contraseña", background_color="#ff375b", pad= (0,0), justification = "center")],
        [sg.Input(key='INPUT2', size=(20, 1))]
    ]
    
    inner_frame = sg.Frame("", inner_frame_layout, background_color='#ff375b', pad = (0,0))

    layout = [
        [texto1],
        [sg.Column([[inner_frame]], justification='center', pad= (0,0))],  # Centrar el marco interno
        [sg.Column([[sg.Image(filename='airbnb.png', size=(200, 200), pad= (0,0))]], justification='center')]  # Centrar la imagen
    ]

    frame = sg.Frame('Varios Elementos', layout, key='FRAME1', size=(960, 540), background_color='#fff')

    return frame

layout = [[marco1()]]

def main():
    frame1 = marco1()
    layout = [[frame1]]
    window = sg.Window('Window Title',layout,size=(960, 540))    
        
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

    window.close()
    
main()    

