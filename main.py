import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt
from marcos import marco1, marco2, marco3, marco4, marco5, marco6
from Graficas_Evidencia import pastel, barras, hist, boxplot
from mapas import abrir_google_maps
from stats import estadistica

def main():
    df = pd.read_csv("CDMXLimpio.csv")
    print(df)

    dfp = pd.read_csv("PragueLimpio.csv")
    print(dfp)

    ventana_principal = sg.Window('Pagina de Inicio', [[marco1.marco1()]], size=(960, 540))
    current_page = 'inicio'

    while True:
        event, values = ventana_principal.read()

        if event == sg.WIN_CLOSED:
            break

        if current_page == 'inicio':
            if event == 'LOGIN' and int(values['PASSWORD']) == 34:
                current_page = 'menu'
                ventana_principal.close()
                ventana_principal = sg.Window('MENU', [[marco2.marco2()]], size=(960, 540))
        elif current_page == 'menu':
            if event == 'LOGOUT':
                current_page = 'inicio'
                ventana_principal.close()
                ventana_principal = sg.Window('Pagina de Inicio', [[marco1.marco1()]], size=(960, 540))
            if event == 'REGRESAR':
                current_page = 'menu'
                ventana_principal.close()
                ventana_principal = sg.Window('MENU', [[marco2.marco2()]], size=(960, 540))
            elif event == 'GRAFICOS':
                ventana_principal.close()
                ventana_graficos = sg.Window('GRAFICOS', [[marco3.marco3()]], size=(960, 540))
                while True:
                    event2, _ = ventana_graficos.read()
                    if event2 == sg.WIN_CLOSED:
                        ventana_graficos.close()
                        break
                    elif event2 == "BUTTON3":
                        pastel()
                    elif event2 == "BUTTON4":
                        barras()
                    elif event2 == "BUTTON5":
                        hist()
                    elif event2 == "BUTTON6":
                        boxplot()
                    elif event2 == "REGRESAR":
                        ventana_graficos.close()
                        ventana_principal = sg.Window('MENU', [[marco2.marco2()]], size=(960, 540))  
            elif event == 'MAPAS':
                ventana_principal.close()
                ventana_mapas = sg.Window('MAPAS', [[marco4.marco4()]], size=(960, 540))
                while True:
                    event2, _ = ventana_mapas.read()
                    if event2 == sg.WIN_CLOSED:
                        ventana_mapas.close()
                        break
                    elif event2 == "BUTTON3":
                        location = "Praga 1"
                        abrir_google_maps(location)
                    elif event2 == "BUTTON4":
                        location = "Praga 2"
                        abrir_google_maps(location)
                    elif event2 == "BUTTON5":
                        location = "Praga 3"
                        abrir_google_maps(location)
                    elif event2 == "BUTTON6":
                        location = "Praga 5"
                        abrir_google_maps(location)
                    elif event2 == "REGRESAR":
                        ventana_mapas.close()
                        ventana_principal = sg.Window('MENU', [[marco2.marco2()]], size=(960, 540)) 
            elif event == 'ANALISIS':
                ventana_principal.close()
                ventana_analisis = sg.Window('ANALISIS DE DATOS', [[marco5.marco5()]], size=(960, 540))
                while True:
                    event2, values = ventana_analisis.read()

                    if event2 == sg.WIN_CLOSED:
                        ventana_analisis.close()
                        break
                    elif values['DESCRIPCION'] == "Precio":
                        
                        estadistica.price()
                        
                    elif values['DESCRIPCION'] == "Tasa de respuesta del anfitrión":
                    
                        estadistica.respuesta()
                        
                    elif values['DESCRIPCION'] == "Tasa de aceptación del anfitrión":
                    
                        estadistica.aceptacion()
                        
                    elif values['DESCRIPCION'] == "Capacidad de la propiedad":
                    
                        estadistica.capacidad()
                        
                    elif values['DESCRIPCION'] == "Puntuación rating":
                    
                        estadistica.rating()
                        
                    elif values['DESCRIPCION'] == "Puntuación precisión":
                    
                        estadistica.accuracy()
                        
                    elif values['DESCRIPCION'] == "Puntuación limpieza":
                    
                        estadistica.limpieza()
                        
                    elif values['DESCRIPCION'] == "Puntuación check in":
                    
                        estadistica.checkin()
                        
                    elif values['DESCRIPCION'] == "Puntuación ubicación":
                    
                        estadistica.ubicación()
                        
                    elif values['DESCRIPCION'] == "Puntuación valor de la propiedad":
                    
                        estadistica.propiedad()
                        
                    elif values['DESCRIPCION'] == "Puntuación comunicación host":
                    
                        estadistica.comunicacion()
                        
                    elif values['DESCRIPCION'] == "Mínimo de noches":
                    
                        estadistica.minimo()
                        
                    elif values['DESCRIPCION'] == "Máximo de noches":
                    
                        estadistica.maximo()
                        
                    elif values['DESCRIPCION'] == "Reviews por mes":
                    
                        estadistica.reviews()

                    elif event2 == "REGRESAR":
                        ventana_analisis.close()
                        ventana_principal = sg.Window('MENU', [[marco2.marco2()]], size=(960, 540))  
            elif event == 'INFORMACION':
                ventana_principal.close()
                ventana_principal = sg.Window('INFORMACION DEL EQUIPO', [[marco6.marco6()]], size=(960, 540))

    ventana_principal.close()

if __name__ == "__main__":
    main()
