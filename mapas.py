import webbrowser

def abrir_google_maps(location):
    url = f"https://www.google.com/maps/place/{location}"
    webbrowser.open(url)
    ubicación = location
