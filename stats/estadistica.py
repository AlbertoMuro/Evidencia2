import pandas as pd
def price():
    #Precio
    CDMXLimpio = pd.read_csv("CDMXLimpio.csv")
    PragueLimpio = pd.read_csv("PragueLimpio.csv")
    precio_df1 = PragueLimpio['price'].mean()
    precio_df2 = CDMXLimpio['price'].mean()
    # Calcular la diferencia numérica entre las medias
    diferencia = round(abs(precio_df1 - precio_df2),2)

    print(f"Precio promedio en Praga: ${round(precio_df1,2)}")
    print(f"Precio promedio en CDMX: ${round(precio_df2,2)}")

    if precio_df1 > precio_df2:
        print(f"La media del precio por alojamiento en Praga es mayor, se espera gastar ${diferencia} mas por noche en comparación a CDMX.")
    elif precio_df1 < precio_df2:
        print(f"La media del precio por alojamiento en CDMX es mayor, se espera gastar ${diferencia} mas por noche en comparación a Praga.")
    else:
        print("El promedio del precio por alojamiento es el mismo.")