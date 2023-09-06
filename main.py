import PySimpleGUI as sg
from marcos import marco1, marco2, marco3, marco4, marco5, marco6

def main():
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
                ventana_principal = sg.Window('GRAFICOS', [[marco3.marco3()]], size=(960, 540))
            elif event == 'MAPAS':
                ventana_principal.close()
                ventana_principal = sg.Window('MAPAS', [[marco4.marco4()]], size=(960, 540))
            elif event == 'ANALISIS':
                ventana_principal.close()
                ventana_principal = sg.Window('ANALISIS DE DATOS', [[marco5.marco5()]], size=(960, 540))
            elif event == 'INFORMACION':
                ventana_principal.close()
                ventana_principal = sg.Window('INFORMACION DEL EQUIPO', [[marco6.marco6()]], size=(960, 540))

    ventana_principal.close()

if __name__ == "__main__":
    main()
