import pandas as pd


def price():
    #Precio
    CDMXLimpio = pd.read_csv("CDMXLimpio.csv")
    PragueLimpio = pd.read_csv("PragueLimpio.csv")
    precio_df1 = PragueLimpio['price'].mean()
    precio_df2 = CDMXLimpio['price'].mean()
    mediana_df1= PragueLimpio['price'].median()
    mediana_df2 = CDMXLimpio['price'].median()
    moda_df1=PragueLimpio['price'].mode()
    moda_df2=CDMXLimpio['price'].mode()
    min_df1=PragueLimpio['price'].min()
    min_df2=CDMXLimpio['price'].min()
    max_df1=PragueLimpio['price'].max()
    max_df2=CDMXLimpio['price'].max()
    
    # Calcular la diferencia numérica entre las medias
    dif_precio = round(abs(precio_df1 - precio_df2),2)
    dif_median = round(abs(mediana_df1 - mediana_df2),2)
    dif_mode = round(abs(moda_df1 - moda_df2),2)
    dif_min = round(abs(min_df1 - min_df2),2)
    dif_max = round(abs(max_df1 - max_df2),2)
   
    
    
    
    print("\nAnálisis de precios en la ciudad de Praga")
    print(f"El precio promedio por alquiler en Praga es de ${round(precio_df1,2)}")
    print(f"La mediana del alquiler en Praga es de ${round( mediana_df1,2)}")
    print(f"El valor modal en Praga es de ${round( moda_df1,2)}")
    print(f"El valor minimo en Praga es de ${( min_df1)}")
    print(f"El valor máximo en Praga es de ${round( max_df1,2)}")
    
    print("\nAnálisis de precios en la CDMX")
    print(f"El precio promedio por alquiler en CDMX es de ${round(precio_df2,2)}")
    print(f"La mediana del alquiler en CDMX es de ${round( mediana_df2,2)}")
    print(f"El valor modal en CDMX es de ${round( moda_df2,2)}")
    print(f"El valor minimo en CDMX es de ${round( min_df2,2)}")
    print(f"El valor máximo en CDMX es de ${round( max_df2,2)}")
    
    print('\nComparación de las ciudades')
    if precio_df1 > precio_df2:
        print(f"La media del precio por alojamiento en Praga es mayor, se espera gastar ${dif_precio} mas por noche en comparación a CDMX.")
    elif precio_df1 < precio_df2:
        print(f"La media del precio por alojamiento en CDMX es mayor, se espera gastar ${dif_precio} mas por noche en comparación a Praga.")
    else:
        print("El promedio del precio por alojamiento es el mismo.")
        

    if mediana_df1 > mediana_df2:
        print(f"La mediana del precio por alojamiento en Praga es mayor, se espera gastar ${dif_median} mas por noche en comparación a CDMX.")
    elif mediana_df1 < mediana_df2:
        print(f"La mediana del precio por alojamiento en CDMX es mayor, se espera gastar ${dif_median} mas por noche en comparación a Praga.")
    else:
        print("El valor de la mediana del precio por alojamiento es el mismo en ambas ciudades.")
        
        
    if min_df1 > min_df2:
        print(f"El valor mínimo registrado del precio por alojamiento en Praga es mayor, la diferencia fue de ${dif_min} mas por noche en comparación a CDMX.")
    elif min_df1 < min_df2:
        print(f"El valor mínimo registrado del precio por alojamiento en CDMX es mayor, la diferencia fue de ${dif_min} mas por noche en comparación a Praga.")
    else:
        print("El valor mínimo registrado del precio por alojamiento fue el mismo en ambas ciudades.")
    
    if max_df1 > max_df2:
        print(f"El valor máximo registrado del precio por alojamiento en Praga es mayor, la diferencia fue de ${dif_max} mas por noche en comparación a CDMX.")
    elif max_df1 < max_df2:
        print(f"El valor máximo registrado del precio por alojamiento en CDMX es mayor, la diferencia fue de ${dif_max} mas por noche en comparación a Praga.")
    else:
        print("El valor máximo registrado del precio por alojamiento fue el mismo en ambas ciudades.")

def respuesta():
    CDMXLimpio = pd.read_csv("CDMXLimpio.csv")
    PragueLimpio = pd.read_csv("PragueLimpio.csv")
    media_df1 = (PragueLimpio['host_response_rate'].mean())*100
    media_df2 = (CDMXLimpio['host_response_rate'].mean())*100
    mediana_df1= (PragueLimpio['host_response_rate'].median())*100
    mediana_df2 = (CDMXLimpio['host_response_rate'].median())*100
    moda_df1=(PragueLimpio['host_response_rate'].mode())*100
    moda_df2=(CDMXLimpio['host_response_rate'].mode())*100
    min_df1=(PragueLimpio['host_response_rate'].min())*100
    min_df2=(CDMXLimpio['host_response_rate'].min())*100
    max_df1=(PragueLimpio['host_response_rate'].max())*100
    max_df2=(CDMXLimpio['host_response_rate'].max())*100
    
    
    dif_media = round(abs(media_df1 - media_df2),2)
    dif_median = round(abs(mediana_df1 - mediana_df2),2)
    dif_mode = round(abs(moda_df1 - moda_df2),2)
    dif_min = round(abs(min_df1 - min_df2),2)
    dif_max = round(abs(max_df1 - max_df2),2)
   
    
    
    
    print("\nAnálisis de porcentaje de respuesta por los anfitriones en la ciudad de Praga")
    print(f"El porcentaje promedio de respuesta por los anfitriones en Praga es de {round(media_df1,2)} %")
    print(f"La mediana del porcentaje de respuesta por los anfitriones en Praga es de {round( mediana_df1,2)} %")
    print(f"El valor(es) modal(es) del porcentaje de respuesta por los anfitriones en Praga es(son) de {round( moda_df1,2)} %")
    print(f"El valor minimo del porcentaje de respuesta por los anfitriones en Praga es de {round( min_df1,2)} %")
    print(f"El valor máximo del porcentaje de respuesta por los anfitriones en Praga es de {round( max_df1,2)} %")
    
    print("\nAnálisis de porcentaje de respuesta por los anfitriones en la CDMX")
    print(f"El porcentaje promedio de respuesta por los anfitriones en CDMX es de {round(media_df2,2)} %")
    print(f"La mediana del porcentaje de respuesta por los anfitriones en CDMX es de {round( mediana_df2,2)} %")
    print(f"El valor modal del porcentaje de respuesta por los anfitriones en CDMX es de {round( moda_df2,2)} %")
    print(f"El valor minimo del porcentaje de respuesta por los anfitriones en CDMX es de {round( min_df2,2)} %")
    print(f"El valor máximo del porcentaje de respuesta por los anfitriones en CDMX es de {round( max_df2,2)} %")
    
    print('\nComparación de las ciudades')
    if media_df1 > media_df2:
        print(f"La media del porcentaje de respuesta por el anfitrión en Praga es mayor, se espera responder {dif_media} % mas a los usuarios en comparación a CDMX.")
    elif media_df1 < media_df2:
        print(f"La media del porcentaje de respuesta por el anfitrión en CDMX es mayor, se espera responder {dif_media} % mas a los usuarios en comparación a Praga.")
    else:
        print("La media del porcentaje de respuesta por el anfitrión es el mismo en ambas ciudades.")
        

    if mediana_df1 > mediana_df2:
        print(f"La mediana del porcentaje de respuesta por los anfitriones en Praga es mayor, se espera responder {dif_median} % mas a los usuarios en comparación a CDMX")
    elif mediana_df1 < mediana_df2:
        print(f"La mediana del porcentaje de respuesta por los anfitriones en CDMX es mayor, se espera responder {dif_median} % mas a los usuarios en comparación a Praga.")
    else:
        print("El valor de la mediana del porcentaje de respuesta por los anfitriones es el mismo en ambas ciudades.")
        
        
    if min_df1 > min_df2:
        print(f"El valor mínimo registrado del porcentaje de respuesta por los anfitriones en Praga es mayor, la diferencia fue de {dif_min} % mas a los usuarios en comparación a CDMX.")
    elif min_df1 < min_df2:
        print(f"El valor mínimo registrado del porcentaje de respuesta por los anfitriones en CDMX es mayor, la diferencia fue de {dif_min} % mas a los usuarios en comparación a Praga.")
    else:
        print("El valor mínimo registrado del porcentaje de respuesta por los anfitriones fue el mismo en ambas ciudades.")
    
    if max_df1 > max_df2:
        print(f"El valor máximo registrado del porcentaje de respuesta por los anfitriones en Praga es mayor, la diferencia fue de {dif_max} % mas a los usuarios en comparación a CDMX.")
    elif max_df1 < max_df2:
        print(f"El valor máximo registrado del porcentaje de respuesta por los anfitriones en CDMX es mayor, la diferencia fue de {dif_max} % mas a los usuarios en comparación a Praga.")
    else:
        print("El valor máximo registrado del porcentaje de respuesta por los anfitriones fue el mismo en ambas ciudades.")
        
        
def aceptacion():
    #Precio
    CDMXLimpio = pd.read_csv("CDMXLimpio.csv")
    PragueLimpio = pd.read_csv("PragueLimpio.csv")
    media_df1 = (PragueLimpio['host_acceptance_rate'].mean())*100
    media_df2 = (CDMXLimpio['host_acceptance_rate'].mean())*100
    mediana_df1= (PragueLimpio['host_acceptance_rate'].median())*100
    mediana_df2 = (CDMXLimpio['host_acceptance_rate'].median())*100
    moda_df1=(PragueLimpio['host_acceptance_rate'].mode())*100
    moda_df2=(CDMXLimpio['host_acceptance_rate'].mode())*100
    min_df1=(PragueLimpio['host_acceptance_rate'].min())*100
    min_df2=(CDMXLimpio['host_acceptance_rate'].min())*100
    max_df1=(PragueLimpio['host_acceptance_rate'].max())*100
    max_df2=(CDMXLimpio['host_acceptance_rate'].max())*100
    
    # Calcular la diferencia numérica entre las medias
    dif_media = round(abs(media_df1 - media_df2),2)
    dif_median = round(abs(mediana_df1 - mediana_df2),2)
    dif_mode = round(abs(moda_df1 - moda_df2),2)
    dif_min = round(abs(min_df1 - min_df2),2)
    dif_max = round(abs(max_df1 - max_df2),2)
   
    
    
    
    print("\nAnálisis de porcentaje de aceptación por los anfitriones en la ciudad de Praga")
    print(f"El porcentaje promedio de aceptación por los anfitriones en Praga es de {round(media_df1,2)} %")
    print(f"La mediana del porcentaje de aceptación por los anfitriones en Praga es de {round( mediana_df1,2)} %")
    print(f"El valor(es) modal(es) del porcentaje de aceptación por los anfitriones en Praga es(son) de {round( moda_df1,2)} %")
    print(f"El valor minimo del porcentaje de aceptación por los anfitriones en Praga es de {round( min_df1,2)} %")
    print(f"El valor máximo del porcentaje de aceptación por los anfitriones en Praga es de {round( max_df1,2)} %")
    
    print("\nAnálisis de porcentaje de aceptación por los anfitriones en la CDMX")
    print(f"El porcentaje promedio de aceptación por los anfitriones en CDMX es de {round(media_df2,2)} %")
    print(f"La mediana del porcentaje de aceptación por los anfitriones en CDMX es de {round( mediana_df2,2)} %")
    print(f"El valor modal del porcentaje de aceptación por los anfitriones en CDMX es de {round( moda_df2,2)} %")
    print(f"El valor minimo del porcentaje de aceptación por los anfitriones en CDMX es de {round( min_df2,2)} %")
    print(f"El valor máximo del porcentaje de aceptación por los anfitriones en CDMX es de {round( max_df2,2)} %")
    
    print('\nComparación de las ciudades')
    if media_df1 > media_df2:
        print(f"La media del porcentaje de aceptación por el anfitrión en Praga es mayor, se espera aceptar {dif_media} % mas a los usuarios en comparación a CDMX.")
    elif media_df1 < media_df2:
        print(f"La media del porcentaje de aceptación por el anfitrión en CDMX es mayor, se espera aceptar {dif_media} % mas a los usuarios en comparación a Praga.")
    else:
        print("La media del porcentaje de aceptación por el anfitrión es el mismo en ambas ciudades.")
        

    if mediana_df1 > mediana_df2:
        print(f"La mediana del porcentaje de aceptación por los anfitriones en Praga es mayor, se espera aceptar {dif_median} % mas a los usuarios en comparación a CDMX")
    elif mediana_df1 < mediana_df2:
        print(f"La mediana del porcentaje de aceptación por los anfitriones en CDMX es mayor, se espera aceptar {dif_median} % mas a los usuarios en comparación a Praga.")
    else:
        print("El valor de la mediana del porcentaje de aceptación por los anfitriones es el mismo en ambas ciudades.")
        
        
    if min_df1 > min_df2:
        print(f"El valor mínimo registrado del porcentaje de aceptación por los anfitriones en Praga es mayor, la diferencia fue de {dif_min} % mas a los usuarios en comparación a CDMX.")
    elif min_df1 < min_df2:
        print(f"El valor mínimo registrado del porcentaje de aceptación por los anfitriones en CDMX es mayor, la diferencia fue de {dif_min} % mas a los usuarios en comparación a Praga.")
    else:
        print("El valor mínimo registrado del porcentaje de aceptación por los anfitriones fue el mismo en ambas ciudades.")
    
    if max_df1 > max_df2:
        print(f"El valor máximo registrado del porcentaje de aceptación por los anfitriones en Praga es mayor, la diferencia fue de {dif_max} % mas a los usuarios en comparación a CDMX.")
    elif max_df1 < max_df2:
        print(f"El valor máximo registrado del porcentaje de aceptación por los anfitriones en CDMX es mayor, la diferencia fue de {dif_max} % mas a los usuarios en comparación a Praga.")
    else:
        print("El valor máximo registrado del porcentaje de aceptación por los anfitriones fue el mismo en ambas ciudades.")       

def capacidad():
    
    CDMXLimpio = pd.read_csv("CDMXLimpio.csv")
    PragueLimpio = pd.read_csv("PragueLimpio.csv")
    media_df1 = PragueLimpio['capacity'].mean()
    media_df2 = CDMXLimpio['capacity'].mean()
    mediana_df1= PragueLimpio['capacity'].median()
    mediana_df2 = CDMXLimpio['capacity'].median()
    moda_df1=PragueLimpio['capacity'].mode()
    moda_df2=CDMXLimpio['capacity'].mode()
    min_df1=PragueLimpio['capacity'].min()
    min_df2=CDMXLimpio['capacity'].min()
    max_df1=PragueLimpio['capacity'].max()
    max_df2=CDMXLimpio['capacity'].max()
    
    # Calcular la diferencia numérica entre las medias
    dif_media = round(abs(media_df1 - media_df2),2)
    dif_mediana = round(abs(mediana_df1 - mediana_df2),2)
    dif_mode = round(abs(moda_df1 - moda_df2),2)
    dif_min = round(abs(min_df1 - min_df2),2)
    dif_max = round(abs(max_df1 - max_df2),2)
   
    
    
    
    print("\nAnálisis de capacidad por propiedad en la ciudad de Praga")
    print(f"La capacidad promedio por alquiler en Praga es de {round(media_df1,2)} personas.")
    print(f"El valor de la mediana para la capacidad del alquiler en Praga es de {round( mediana_df1,2)} personas.")
    print(f"El valor(es) modal(es) en Praga es(son) de {round( moda_df1,2)} personas.")
    print(f"El valor minimo para la capacidad en la ciudad de Praga es de {( min_df1)} personas.")
    print(f"El valor máximo para la capacidad en la ciudad de Praga es de {round( max_df1,2)} personas.")
    
    print("\nAnálisis de capacidad por propiedad en la CDMX")
    print(f"La capacidad promedio por alquiler en CDMX es de {round(media_df2,2)} personas.")
    print(f"El valor de la mediana para la capacidad del alquiler en CDMX es de {round( mediana_df2,2)} personas.")
    print(f"El valor(es) modal(es) en CDMX es(son) de {round( moda_df2,2)} personas.")
    print(f"El valor minimo para la capacidad en la ciudad de CDMX es de {( min_df2)} personas.")
    print(f"El valor máximo para la capacidad en la ciudad de CDMX es de {round( max_df2,2)} personas.")    
    
    
    print('\nComparación de las ciudades')
    if media_df1 > media_df2:
        print(f"La media de la capacidad promedio por alquiler en Praga es mayor, se espera alojar a {dif_media} personas mas por noche en comparación a CDMX.")
    elif media_df1 < media_df2:
        print(f"La media de la capacidad promedio por alquiler en CDMX es mayor, se espera alojar {dif_media} personas mas por noche en comparación a Praga.")
    else:
        print("El promedio de personas esperadas por alojamiento es el mismo para ambas ciudades.")
        

    if mediana_df1 > mediana_df2:
        print(f"El valor de la mediana de la capacidad promedio por alquiler en Praga es mayor, se espera alojar a {dif_mediana} personas mas por noche en comparación a CDMX.")
    elif mediana_df1 < mediana_df2:
        print(f"El valor de la mediana de la capacidad promedio por alquiler CDMX es mayor, se espera alojar {dif_mediana} personas mas por noche en comparación a Praga.")
    else:
        print("El valor de la mediana de personas esperadas por alojamiento es el mismo en ambas ciudades.")
        
        
    if min_df1 > min_df2:
        print(f"El valor mínimo registrado de personas esperadas por alojamiento en Praga es mayor, la diferencia de personas alojadas fue de {dif_min} mas por noche en comparación a CDMX.")
    elif min_df1 < min_df2:
        print(f"El valor mínimo registrado de personas esperadas por alojamiento en CDMX es mayor, la diferencia de personas fue de {dif_min} mas por noche en comparación a Praga.")
    else:
        print("El valor mínimo registrado de personas esperadas por alojamiento  fue el mismo en ambas ciudades.")
    
    if max_df1 > max_df2:
        print(f"El valor máximo registrado de personas esperadas por alojamiento  en Praga es mayor, la diferencia de personas fue de {dif_max} mas por noche en comparación a CDMX.")
    elif max_df1 < max_df2:
        print(f"El valor máximo registrado de personas esperadas por alojamiento  en CDMX es mayor, la diferencia de personas fue de {dif_max} mas por noche en comparación a Praga.")
    else:
        print("El valor máximo registrado de personas esperadas por alojamiento fue el mismo en ambas ciudades.")
        
        
def rating():
    #Precio
    CDMXLimpio = pd.read_csv("CDMXLimpio.csv")
    PragueLimpio = pd.read_csv("PragueLimpio.csv")
    media_df1 = PragueLimpio['review_scores_rating'].mean()
    media_df2 = CDMXLimpio['review_scores_rating'].mean()
    mediana_df1= PragueLimpio['review_scores_rating'].median()
    mediana_df2 = CDMXLimpio['review_scores_rating'].median()
    moda_df1=PragueLimpio['review_scores_rating'].mode()
    moda_df2=CDMXLimpio['review_scores_rating'].mode()
    min_df1=PragueLimpio['review_scores_rating'].min()
    min_df2=CDMXLimpio['review_scores_rating'].min()
    max_df1=PragueLimpio['review_scores_rating'].max()
    max_df2=CDMXLimpio['review_scores_rating'].max()
    
    # Calcular la diferencia numérica entre las medias
    dif_media = round(abs(media_df1 - media_df2),2)
    dif_mediana = round(abs(mediana_df1 - mediana_df2),2)
    dif_mode = round(abs(moda_df1 - moda_df2),2)
    dif_min = round(abs(min_df1 - min_df2),2)
    dif_max = round(abs(max_df1 - max_df2),2)
   
    
    
    
    print("\nAnálisis de puntuación de rating asignado por los usuarios  en la ciudad de Praga.")
    print(f"La puntuación promedio en Praga es de {round(media_df1,2)}.")
    print(f"El valor de la mediana en Praga es de {round( mediana_df1,2)}.")
    print(f"El valor(es) modal(es) en Praga es(son) de {round( moda_df1,2)}.")
    print(f"El valor minimo en la ciudad de Praga es de {( min_df1)}.")
    print(f"El valor máximo en la ciudad de Praga es de {round( max_df1,2)}.")
    
    print("\nAnálisis de puntuación de rating asignado por los usuarios en la CDMX")
    print(f"La puntuación promedio en CDMX es de {round(media_df2,2)}.")
    print(f"El valor de la mediana en CDMX es de {round( mediana_df2,2)}.")
    print(f"El valor(es) modal(es) en CDMX es(son) de {round( moda_df2,2)}.")
    print(f"El valor minimo en la ciudad de CDMX es de {( min_df2)}.")
    print(f"El valor máximo en la ciudad de CDMX es de {round( max_df2,2)}.")    
    
    
    print('\nComparación de las ciudades')
    if media_df1 > media_df2:
        print(f"La media de puntuación en Praga es mayor, la diferencia es de {dif_media} puntos en comparación a CDMX.")
    elif media_df1 < media_df2:
        print(f"La media de puntuación en CDMX es mayor, la diferencia fue de {dif_media} puntos en comparación a Praga.")
    else:
        print("El promedio de puntuación es el mismo para ambas ciudades.")
        

    if mediana_df1 > mediana_df2:
        print(f"El valor de la mediana de la puntuación en Praga es mayor, la diferencia es de {dif_mediana} puntos en comparación a CDMX.")
    elif mediana_df1 < mediana_df2:
        print(f"El valor de la mediana de la puntuación en CDMX es mayor, la diferencia es de {dif_mediana} puntos en comparación a Praga.")
    else:
        print("El valor de la mediana de la puntuación es el mismo en ambas ciudades.")
        
        
    if min_df1 > min_df2:
        print(f"El valor mínimo de la puntuación en Praga fue mayor, la diferencia fue de {dif_min} puntos mas en comparación a CDMX.")
    elif min_df1 < min_df2:
        print(f"El valor mínimo de la puntuación en CDMX fue mayor, la diferencia fue de {dif_min} puntos mas en comparación a Praga.")
    else:
        print("El valor mínimo registrado de puntos fue el mismo en ambas ciudades.")
    
    if max_df1 > max_df2:
        print(f"El valor máximo de la puntuación en Praga es mayor, la diferencia fue de {dif_max} puntos mas en comparación a CDMX.")
    elif max_df1 < max_df2:
        print(f"El valor máximo de la puntuación en CDMX es mayor, la diferencia fue de {dif_max} puntos mas en comparación a Praga.")
    else:
        print("El valor máximo registrado de la puntuación fue el mismo en ambas ciudades.")
        

def accuracy():
    #Precio
    CDMXLimpio = pd.read_csv("CDMXLimpio.csv")
    PragueLimpio = pd.read_csv("PragueLimpio.csv")
    media_df1 = PragueLimpio['review_scores_accuracy'].mean()
    media_df2 = CDMXLimpio['review_scores_accuracy'].mean()
    mediana_df1= PragueLimpio['review_scores_accuracy'].median()
    mediana_df2 = CDMXLimpio['review_scores_accuracy'].median()
    moda_df1=PragueLimpio['review_scores_accuracy'].mode()
    moda_df2=CDMXLimpio['review_scores_accuracy'].mode()
    min_df1=PragueLimpio['review_scores_accuracy'].min()
    min_df2=CDMXLimpio['review_scores_accuracy'].min()
    max_df1=PragueLimpio['review_scores_accuracy'].max()
    max_df2=CDMXLimpio['review_scores_accuracy'].max()
    
    # Calcular la diferencia numérica entre las medias
    dif_media = round(abs(media_df1 - media_df2),2)
    dif_mediana = round(abs(mediana_df1 - mediana_df2),2)
    dif_mode = round(abs(moda_df1 - moda_df2),2)
    dif_min = round(abs(min_df1 - min_df2),2)
    dif_max = round(abs(max_df1 - max_df2),2)
   
    
    
    
    print("\nAnálisis de puntuación de precisión asignado por los usuarios  en la ciudad de Praga.")
    print(f"La puntuación promedio en Praga es de {round(media_df1,2)}.")
    print(f"El valor de la mediana en Praga es de {round( mediana_df1,2)}.")
    print(f"El valor(es) modal(es) en Praga es(son) de {round( moda_df1,2)}.")
    print(f"El valor minimo en la ciudad de Praga es de {( min_df1)}.")
    print(f"El valor máximo en la ciudad de Praga es de {round( max_df1,2)}.")
    
    print("\nAnálisis de puntuación de presición asignado por los usuarios en la CDMX")
    print(f"La puntuación promedio en CDMX es de {round(media_df2,2)}.")
    print(f"El valor de la mediana en CDMX es de {round( mediana_df2,2)}.")
    print(f"El valor(es) modal(es) en CDMX es(son) de {round( moda_df2,2)}.")
    print(f"El valor minimo en la ciudad de CDMX es de {( min_df2)}.")
    print(f"El valor máximo en la ciudad de CDMX es de {round( max_df2,2)}.")    
    
    
    print('\nComparación de las ciudades')
    if media_df1 > media_df2:
        print(f"La media de puntuación en Praga es mayor, la diferencia es de {dif_media} puntos en comparación a CDMX.")
    elif media_df1 < media_df2:
        print(f"La media de puntuación en CDMX es mayor, la diferencia fue de {dif_media} puntos en comparación a Praga.")
    else:
        print("El promedio de puntuación es el mismo para ambas ciudades.")
        

    if mediana_df1 > mediana_df2:
        print(f"El valor de la mediana de la puntuación en Praga es mayor, la diferencia es de {dif_mediana} puntos en comparación a CDMX.")
    elif mediana_df1 < mediana_df2:
        print(f"El valor de la mediana de la puntuación en CDMX es mayor, la diferencia es de {dif_mediana} puntos en comparación a Praga.")
    else:
        print("El valor de la mediana de la puntuación es el mismo en ambas ciudades.")
        
        
    if min_df1 > min_df2:
        print(f"El valor mínimo de la puntuación en Praga fue mayor, la diferencia fue de {dif_min} puntos mas en comparación a CDMX.")
    elif min_df1 < min_df2:
        print(f"El valor mínimo de la puntuación en CDMX fue mayor, la diferencia fue de {dif_min} puntos mas en comparación a Praga.")
    else:
        print("El valor mínimo registrado de puntos fue el mismo en ambas ciudades.")
    
    if max_df1 > max_df2:
        print(f"El valor máximo de la puntuación en Praga es mayor, la diferencia fue de {dif_max} puntos mas en comparación a CDMX.")
    elif max_df1 < max_df2:
        print(f"El valor máximo de la puntuación en CDMX es mayor, la diferencia fue de {dif_max} puntos mas en comparación a Praga.")
    else:
        print("El valor máximo registrado de la puntuación fue el mismo en ambas ciudades.")
        
def limpieza():
    #Precio
    CDMXLimpio = pd.read_csv("CDMXLimpio.csv")
    PragueLimpio = pd.read_csv("PragueLimpio.csv")
    media_df1 = PragueLimpio['review_scores_cleanliness'].mean()
    media_df2 = CDMXLimpio['review_scores_cleanliness'].mean()
    mediana_df1= PragueLimpio['review_scores_cleanliness'].median()
    mediana_df2 = CDMXLimpio['review_scores_cleanliness'].median()
    moda_df1=PragueLimpio['review_scores_cleanliness'].mode()
    moda_df2=CDMXLimpio['review_scores_cleanliness'].mode()
    min_df1=PragueLimpio['review_scores_cleanliness'].min()
    min_df2=CDMXLimpio['review_scores_cleanliness'].min()
    max_df1=PragueLimpio['review_scores_cleanliness'].max()
    max_df2=CDMXLimpio['review_scores_cleanliness'].max()
    
    # Calcular la diferencia numérica entre las medias
    dif_media = round(abs(media_df1 - media_df2),2)
    dif_mediana = round(abs(mediana_df1 - mediana_df2),2)
    dif_mode = round(abs(moda_df1 - moda_df2),2)
    dif_min = round(abs(min_df1 - min_df2),2)
    dif_max = round(abs(max_df1 - max_df2),2)
   
    
    
    
    print("\nAnálisis de puntuación de limpieza asignado por los usuarios  en la ciudad de Praga.")
    print(f"La puntuación promedio en Praga es de {round(media_df1,2)}.")
    print(f"El valor de la mediana en Praga es de {round( mediana_df1,2)}.")
    print(f"El valor(es) modal(es) en Praga es(son) de {round( moda_df1,2)}.")
    print(f"El valor minimo en la ciudad de Praga es de {( min_df1)}.")
    print(f"El valor máximo en la ciudad de Praga es de {round( max_df1,2)}.")
    
    print("\nAnálisis de puntuación de limpieza asignado por los usuarios en la CDMX")
    print(f"La puntuación promedio en CDMX es de {round(media_df2,2)}.")
    print(f"El valor de la mediana en CDMX es de {round( mediana_df2,2)}.")
    print(f"El valor(es) modal(es) en CDMX es(son) de {round( moda_df2,2)}.")
    print(f"El valor minimo en la ciudad de CDMX es de {( min_df2)}.")
    print(f"El valor máximo en la ciudad de CDMX es de {round( max_df2,2)}.")    
    
    
    print('\nComparación de las ciudades')
    if media_df1 > media_df2:
        print(f"La media de puntuación en Praga es mayor, la diferencia es de {dif_media} puntos en comparación a CDMX.")
    elif media_df1 < media_df2:
        print(f"La media de puntuación en CDMX es mayor, la diferencia fue de {dif_media} puntos en comparación a Praga.")
    else:
        print("El promedio de puntuación es el mismo para ambas ciudades.")
        

    if mediana_df1 > mediana_df2:
        print(f"El valor de la mediana de la puntuación en Praga es mayor, la diferencia es de {dif_mediana} puntos en comparación a CDMX.")
    elif mediana_df1 < mediana_df2:
        print(f"El valor de la mediana de la puntuación en CDMX es mayor, la diferencia es de {dif_mediana} puntos en comparación a Praga.")
    else:
        print("El valor de la mediana de la puntuación es el mismo en ambas ciudades.")
        
        
    if min_df1 > min_df2:
        print(f"El valor mínimo de la puntuación en Praga fue mayor, la diferencia fue de {dif_min} puntos mas en comparación a CDMX.")
    elif min_df1 < min_df2:
        print(f"El valor mínimo de la puntuación en CDMX fue mayor, la diferencia fue de {dif_min} puntos mas en comparación a Praga.")
    else:
        print("El valor mínimo registrado de puntos fue el mismo en ambas ciudades.")
    
    if max_df1 > max_df2:
        print(f"El valor máximo de la puntuación en Praga es mayor, la diferencia fue de {dif_max} puntos mas en comparación a CDMX.")
    elif max_df1 < max_df2:
        print(f"El valor máximo de la puntuación en CDMX es mayor, la diferencia fue de {dif_max} puntos mas en comparación a Praga.")
    else:
        print("El valor máximo registrado de la puntuación fue el mismo en ambas ciudades.")
        
def checkin():
    #Precio
    CDMXLimpio = pd.read_csv("CDMXLimpio.csv")
    PragueLimpio = pd.read_csv("PragueLimpio.csv")
    media_df1 = PragueLimpio['review_scores_checkin'].mean()
    media_df2 = CDMXLimpio['review_scores_checkin'].mean()
    mediana_df1= PragueLimpio['review_scores_checkin'].median()
    mediana_df2 = CDMXLimpio['review_scores_checkin'].median()
    moda_df1=PragueLimpio['review_scores_checkin'].mode()
    moda_df2=CDMXLimpio['review_scores_checkin'].mode()
    min_df1=PragueLimpio['review_scores_checkin'].min()
    min_df2=CDMXLimpio['review_scores_checkin'].min()
    max_df1=PragueLimpio['review_scores_checkin'].max()
    max_df2=CDMXLimpio['review_scores_checkin'].max()
    
    # Calcular la diferencia numérica entre las medias
    dif_media = round(abs(media_df1 - media_df2),2)
    dif_mediana = round(abs(mediana_df1 - mediana_df2),2)
    dif_mode = round(abs(moda_df1 - moda_df2),2)
    dif_min = round(abs(min_df1 - min_df2),2)
    dif_max = round(abs(max_df1 - max_df2),2)
   
    
    
    
    print("\nAnálisis de puntuación de chek in asignado por los usuarios  en la ciudad de Praga.")
    print(f"La puntuación promedio en Praga es de {round(media_df1,2)}.")
    print(f"El valor de la mediana en Praga es de {round( mediana_df1,2)}.")
    print(f"El valor(es) modal(es) en Praga es(son) de {round( moda_df1,2)}.")
    print(f"El valor minimo en la ciudad de Praga es de {( min_df1)}.")
    print(f"El valor máximo en la ciudad de Praga es de {round( max_df1,2)}.")
    
    print("\nAnálisis de puntuación de chek in asignado por los usuarios en la CDMX")
    print(f"La puntuación promedio en CDMX es de {round(media_df2,2)}.")
    print(f"El valor de la mediana en CDMX es de {round( mediana_df2,2)}.")
    print(f"El valor(es) modal(es) en CDMX es(son) de {round( moda_df2,2)}.")
    print(f"El valor minimo en la ciudad de CDMX es de {( min_df2)}.")
    print(f"El valor máximo en la ciudad de CDMX es de {round( max_df2,2)}.")    
    
    
    print('\nComparación de las ciudades')
    if media_df1 > media_df2:
        print(f"La media de puntuación en Praga es mayor, la diferencia es de {dif_media} puntos en comparación a CDMX.")
    elif media_df1 < media_df2:
        print(f"La media de puntuación en CDMX es mayor, la diferencia fue de {dif_media} puntos en comparación a Praga.")
    else:
        print("El promedio de puntuación es el mismo para ambas ciudades.")
        

    if mediana_df1 > mediana_df2:
        print(f"El valor de la mediana de la puntuación en Praga es mayor, la diferencia es de {dif_mediana} puntos en comparación a CDMX.")
    elif mediana_df1 < mediana_df2:
        print(f"El valor de la mediana de la puntuación en CDMX es mayor, la diferencia es de {dif_mediana} puntos en comparación a Praga.")
    else:
        print("El valor de la mediana de la puntuación es el mismo en ambas ciudades.")
        
        
    if min_df1 > min_df2:
        print(f"El valor mínimo de la puntuación en Praga fue mayor, la diferencia fue de {dif_min} puntos mas en comparación a CDMX.")
    elif min_df1 < min_df2:
        print(f"El valor mínimo de la puntuación en CDMX fue mayor, la diferencia fue de {dif_min} puntos mas en comparación a Praga.")
    else:
        print("El valor mínimo registrado de puntos fue el mismo en ambas ciudades.")
    
    if max_df1 > max_df2:
        print(f"El valor máximo de la puntuación en Praga es mayor, la diferencia fue de {dif_max} puntos mas en comparación a CDMX.")
    elif max_df1 < max_df2:
        print(f"El valor máximo de la puntuación en CDMX es mayor, la diferencia fue de {dif_max} puntos mas en comparación a Praga.")
    else:
        print("El valor máximo registrado de la puntuación fue el mismo en ambas ciudades.")
        
def ubicación():
    #Precio
    CDMXLimpio = pd.read_csv("CDMXLimpio.csv")
    PragueLimpio = pd.read_csv("PragueLimpio.csv")
    media_df1 = PragueLimpio['review_scores_location'].mean()
    media_df2 = CDMXLimpio['review_scores_location'].mean()
    mediana_df1= PragueLimpio['review_scores_location'].median()
    mediana_df2 = CDMXLimpio['review_scores_location'].median()
    moda_df1=PragueLimpio['review_scores_location'].mode()
    moda_df2=CDMXLimpio['review_scores_location'].mode()
    min_df1=PragueLimpio['review_scores_location'].min()
    min_df2=CDMXLimpio['review_scores_location'].min()
    max_df1=PragueLimpio['review_scores_location'].max()
    max_df2=CDMXLimpio['review_scores_location'].max()
    
    # Calcular la diferencia numérica entre las medias
    dif_media = round(abs(media_df1 - media_df2),2)
    dif_mediana = round(abs(mediana_df1 - mediana_df2),2)
    dif_mode = round(abs(moda_df1 - moda_df2),2)
    dif_min = round(abs(min_df1 - min_df2),2)
    dif_max = round(abs(max_df1 - max_df2),2)
   
    
    
    
    print("\nAnálisis de puntuación de ubicación asignado por los usuarios  en la ciudad de Praga.")
    print(f"La puntuación promedio en Praga es de {round(media_df1,2)}.")
    print(f"El valor de la mediana en Praga es de {round( mediana_df1,2)}.")
    print(f"El valor(es) modal(es) en Praga es(son) de {round( moda_df1,2)}.")
    print(f"El valor minimo en la ciudad de Praga es de {( min_df1)}.")
    print(f"El valor máximo en la ciudad de Praga es de {round( max_df1,2)}.")
    
    print("\nAnálisis de puntuación de ubicación asignado por los usuarios en la CDMX")
    print(f"La puntuación promedio en CDMX es de {round(media_df2,2)}.")
    print(f"El valor de la mediana en CDMX es de {round( mediana_df2,2)}.")
    print(f"El valor(es) modal(es) en CDMX es(son) de {round( moda_df2,2)}.")
    print(f"El valor minimo en la ciudad de CDMX es de {( min_df2)}.")
    print(f"El valor máximo en la ciudad de CDMX es de {round( max_df2,2)}.")    
    
    
    print('\nComparación de las ciudades')
    if media_df1 > media_df2:
        print(f"La media de puntuación en Praga es mayor, la diferencia es de {dif_media} puntos en comparación a CDMX.")
    elif media_df1 < media_df2:
        print(f"La media de puntuación en CDMX es mayor, la diferencia fue de {dif_media} puntos en comparación a Praga.")
    else:
        print("El promedio de puntuación es el mismo para ambas ciudades.")
        

    if mediana_df1 > mediana_df2:
        print(f"El valor de la mediana de la puntuación en Praga es mayor, la diferencia es de {dif_mediana} puntos en comparación a CDMX.")
    elif mediana_df1 < mediana_df2:
        print(f"El valor de la mediana de la puntuación en CDMX es mayor, la diferencia es de {dif_mediana} puntos en comparación a Praga.")
    else:
        print("El valor de la mediana de la puntuación es el mismo en ambas ciudades.")
        
        
    if min_df1 > min_df2:
        print(f"El valor mínimo de la puntuación en Praga fue mayor, la diferencia fue de {dif_min} puntos mas en comparación a CDMX.")
    elif min_df1 < min_df2:
        print(f"El valor mínimo de la puntuación en CDMX fue mayor, la diferencia fue de {dif_min} puntos mas en comparación a Praga.")
    else:
        print("El valor mínimo registrado de puntos fue el mismo en ambas ciudades.")
    
    if max_df1 > max_df2:
        print(f"El valor máximo de la puntuación en Praga es mayor, la diferencia fue de {dif_max} puntos mas en comparación a CDMX.")
    elif max_df1 < max_df2:
        print(f"El valor máximo de la puntuación en CDMX es mayor, la diferencia fue de {dif_max} puntos mas en comparación a Praga.")
    else:
        print("El valor máximo registrado de la puntuación fue el mismo en ambas ciudades.")
        
def propiedad():
    #Precio
    CDMXLimpio = pd.read_csv("CDMXLimpio.csv")
    PragueLimpio = pd.read_csv("PragueLimpio.csv")
    media_df1 = PragueLimpio['review_scores_value'].mean()
    media_df2 = CDMXLimpio['review_scores_value'].mean()
    mediana_df1= PragueLimpio['review_scores_value'].median()
    mediana_df2 = CDMXLimpio['review_scores_value'].median()
    moda_df1=PragueLimpio['review_scores_value'].mode()
    moda_df2=CDMXLimpio['review_scores_value'].mode()
    min_df1=PragueLimpio['review_scores_value'].min()
    min_df2=CDMXLimpio['review_scores_value'].min()
    max_df1=PragueLimpio['review_scores_value'].max()
    max_df2=CDMXLimpio['review_scores_value'].max()
    
    # Calcular la diferencia numérica entre las medias
    dif_media = round(abs(media_df1 - media_df2),2)
    dif_mediana = round(abs(mediana_df1 - mediana_df2),2)
    dif_mode = round(abs(moda_df1 - moda_df2),2)
    dif_min = round(abs(min_df1 - min_df2),2)
    dif_max = round(abs(max_df1 - max_df2),2)
   
    
    
    
    print("\nAnálisis de puntuación sobre el valor de la propiedad asignado por los usuarios  en la ciudad de Praga.")
    print(f"La puntuación promedio en Praga es de {round(media_df1,2)}.")
    print(f"El valor de la mediana en Praga es de {round( mediana_df1,2)}.")
    print(f"El valor(es) modal(es) en Praga es(son) de {round( moda_df1,2)}.")
    print(f"El valor minimo en la ciudad de Praga es de {( min_df1)}.")
    print(f"El valor máximo en la ciudad de Praga es de {round( max_df1,2)}.")
    
    print("\nAnálisis de puntuación sobre el valor de la propiedad asignado por los usuarios en la CDMX")
    print(f"La puntuación promedio en CDMX es de {round(media_df2,2)}.")
    print(f"El valor de la mediana en CDMX es de {round( mediana_df2,2)}.")
    print(f"El valor(es) modal(es) en CDMX es(son) de {round( moda_df2,2)}.")
    print(f"El valor minimo en la ciudad de CDMX es de {( min_df2)}.")
    print(f"El valor máximo en la ciudad de CDMX es de {round( max_df2,2)}.")    
    
    
    print('\nComparación de las ciudades')
    if media_df1 > media_df2:
        print(f"La media de puntuación en Praga es mayor, la diferencia es de {dif_media} puntos en comparación a CDMX.")
    elif media_df1 < media_df2:
        print(f"La media de puntuación en CDMX es mayor, la diferencia fue de {dif_media} puntos en comparación a Praga.")
    else:
        print("El promedio de puntuación es el mismo para ambas ciudades.")
        

    if mediana_df1 > mediana_df2:
        print(f"El valor de la mediana de la puntuación en Praga es mayor, la diferencia es de {dif_mediana} puntos en comparación a CDMX.")
    elif mediana_df1 < mediana_df2:
        print(f"El valor de la mediana de la puntuación en CDMX es mayor, la diferencia es de {dif_mediana} puntos en comparación a Praga.")
    else:
        print("El valor de la mediana de la puntuación es el mismo en ambas ciudades.")
        
        
    if min_df1 > min_df2:
        print(f"El valor mínimo de la puntuación en Praga fue mayor, la diferencia fue de {dif_min} puntos mas en comparación a CDMX.")
    elif min_df1 < min_df2:
        print(f"El valor mínimo de la puntuación en CDMX fue mayor, la diferencia fue de {dif_min} puntos mas en comparación a Praga.")
    else:
        print("El valor mínimo registrado de puntos fue el mismo en ambas ciudades.")
    
    if max_df1 > max_df2:
        print(f"El valor máximo de la puntuación en Praga es mayor, la diferencia fue de {dif_max} puntos mas en comparación a CDMX.")
    elif max_df1 < max_df2:
        print(f"El valor máximo de la puntuación en CDMX es mayor, la diferencia fue de {dif_max} puntos mas en comparación a Praga.")
    else:
        print("El valor máximo registrado de la puntuación fue el mismo en ambas ciudades.")
        
def comunicacion():
    #Precio
    CDMXLimpio = pd.read_csv("CDMXLimpio.csv")
    PragueLimpio = pd.read_csv("PragueLimpio.csv")
    media_df1 = PragueLimpio['review_scores_communication'].mean()
    media_df2 = CDMXLimpio['review_scores_communication'].mean()
    mediana_df1= PragueLimpio['review_scores_communication'].median()
    mediana_df2 = CDMXLimpio['review_scores_communication'].median()
    moda_df1=PragueLimpio['review_scores_communication'].mode()
    moda_df2=CDMXLimpio['review_scores_communication'].mode()
    min_df1=PragueLimpio['review_scores_communication'].min()
    min_df2=CDMXLimpio['review_scores_communication'].min()
    max_df1=PragueLimpio['review_scores_communication'].max()
    max_df2=CDMXLimpio['review_scores_communication'].max()
    
    # Calcular la diferencia numérica entre las medias
    dif_media = round(abs(media_df1 - media_df2),2)
    dif_mediana = round(abs(mediana_df1 - mediana_df2),2)
    dif_mode = round(abs(moda_df1 - moda_df2),2)
    dif_min = round(abs(min_df1 - min_df2),2)
    dif_max = round(abs(max_df1 - max_df2),2)
   
    
    
    
    print("\nAnálisis de puntuación sobre el contacto con el anfitrión asignado por los usuarios  en la ciudad de Praga.")
    print(f"La puntuación promedio en Praga es de {round(media_df1,2)}.")
    print(f"El valor de la mediana en Praga es de {round( mediana_df1,2)}.")
    print(f"El valor(es) modal(es) en Praga es(son) de {round( moda_df1,2)}.")
    print(f"El valor minimo en la ciudad de Praga es de {( min_df1)}.")
    print(f"El valor máximo en la ciudad de Praga es de {round( max_df1,2)}.")
    
    print("\nAnálisis de puntuación sobre el contacto con el anfitrión asignado por los usuarios en la CDMX")
    print(f"La puntuación promedio en CDMX es de {round(media_df2,2)}.")
    print(f"El valor de la mediana en CDMX es de {round( mediana_df2,2)}.")
    print(f"El valor(es) modal(es) en CDMX es(son) de {round( moda_df2,2)}.")
    print(f"El valor minimo en la ciudad de CDMX es de {( min_df2)}.")
    print(f"El valor máximo en la ciudad de CDMX es de {round( max_df2,2)}.")    
    
    
    print('\nComparación de las ciudades')
    if media_df1 > media_df2:
        print(f"La media de puntuación en Praga es mayor, la diferencia es de {dif_media} puntos en comparación a CDMX.")
    elif media_df1 < media_df2:
        print(f"La media de puntuación en CDMX es mayor, la diferencia fue de {dif_media} puntos en comparación a Praga.")
    else:
        print("El promedio de puntuación es el mismo para ambas ciudades.")
        

    if mediana_df1 > mediana_df2:
        print(f"El valor de la mediana de la puntuación en Praga es mayor, la diferencia es de {dif_mediana} puntos en comparación a CDMX.")
    elif mediana_df1 < mediana_df2:
        print(f"El valor de la mediana de la puntuación en CDMX es mayor, la diferencia es de {dif_mediana} puntos en comparación a Praga.")
    else:
        print("El valor de la mediana de la puntuación es el mismo en ambas ciudades.")
        
        
    if min_df1 > min_df2:
        print(f"El valor mínimo de la puntuación en Praga fue mayor, la diferencia fue de {dif_min} puntos mas en comparación a CDMX.")
    elif min_df1 < min_df2:
        print(f"El valor mínimo de la puntuación en CDMX fue mayor, la diferencia fue de {dif_min} puntos mas en comparación a Praga.")
    else:
        print("El valor mínimo registrado de puntos fue el mismo en ambas ciudades.")
    
    if max_df1 > max_df2:
        print(f"El valor máximo de la puntuación en Praga es mayor, la diferencia fue de {dif_max} puntos mas en comparación a CDMX.")
    elif max_df1 < max_df2:
        print(f"El valor máximo de la puntuación en CDMX es mayor, la diferencia fue de {dif_max} puntos mas en comparación a Praga.")
    else:
        print("El valor máximo registrado de la puntuación fue el mismo en ambas ciudades.")
        
def minimo():
    #Precio
    CDMXLimpio = pd.read_csv("CDMXLimpio.csv")
    PragueLimpio = pd.read_csv("PragueLimpio.csv")
    media_df1 = PragueLimpio['minimum_nights'].mean()
    media_df2 = CDMXLimpio['minimum_nights'].mean()
    mediana_df1= PragueLimpio['minimum_nights'].median()
    mediana_df2 = CDMXLimpio['minimum_nights'].median()
    moda_df1=PragueLimpio['minimum_nights'].mode()
    moda_df2=CDMXLimpio['minimum_nights'].mode()
    min_df1=PragueLimpio['minimum_nights'].min()
    min_df2=CDMXLimpio['minimum_nights'].min()
    max_df1=PragueLimpio['minimum_nights'].max()
    max_df2=CDMXLimpio['minimum_nights'].max()
    
    # Calcular la diferencia numérica entre las medias
    dif_media = round(abs(media_df1 - media_df2),2)
    dif_mediana = round(abs(mediana_df1 - mediana_df2),2)
    dif_mode = round(abs(moda_df1 - moda_df2),2)
    dif_min = round(abs(min_df1 - min_df2),2)
    dif_max = round(abs(max_df1 - max_df2),2)
   
    
    
    
    print("\nAnálisis del mínimo de noches en la ciudad de Praga.")
    print(f"El promedio de mínimo de noches en Praga es de {round(media_df1,2)}.")
    print(f"El valor de la mediana en Praga es de {round( mediana_df1,2)}.")
    print(f"El valor(es) modal(es) en Praga es(son) de {round( moda_df1,2)}.")
    print(f"El valor minimo en la ciudad de Praga es de {( min_df1)}.")
    print(f"El valor máximo en la ciudad de Praga es de {round( max_df1,2)}.")
    
    print("\nAnálisis del mínimo de noches en la CDMX")
    print(f"El promedio de mínimo de noches en CDMX es de {round(media_df2,2)}.")
    print(f"El valor de la mediana en CDMX es de {round( mediana_df2,2)}.")
    print(f"El valor(es) modal(es) en CDMX es(son) de {round( moda_df2,2)}.")
    print(f"El valor minimo en la ciudad de CDMX es de {( min_df2)}.")
    print(f"El valor máximo en la ciudad de CDMX es de {round( max_df2,2)}.")    
    
    
    print('\nComparación de las ciudades')
    if media_df1 > media_df2:
        print(f"La media de mínimo de noches en Praga es mayor, la diferencia es de {dif_media} noches en comparación a CDMX.")
    elif media_df1 < media_df2:
        print(f"La media de mínimo de noches en CDMX es mayor, la diferencia es de {dif_media} noches en comparación a Praga.")
    else:
        print("El promedio de mínimo de noches es el mismo para ambas ciudades.")
        

    if mediana_df1 > mediana_df2:
        print(f"El valor de la mediana para el mínimo de noches en Praga es mayor, la diferencia es de {dif_mediana} noches en comparación a CDMX.")
    elif mediana_df1 < mediana_df2:
        print(f"El valor de la mediana para el mínimo de noches en CDMX es mayor, la diferencia es de {dif_mediana} noches en comparación a Praga.")
    else:
        print("El valor de la mediana para el mínimo de noches es el mismo en ambas ciudades.")
        
        
    if min_df1 > min_df2:
        print(f"El valor mínimo para el mínimo de noches en Praga fue mayor, la diferencia fue de {dif_min} noches mas en comparación a CDMX.")
    elif min_df1 < min_df2:
        print(f"El valor mínimo para el mínimo de noches en CDMX fue mayor, la diferencia fue de {dif_min} noches mas en comparación a Praga.")
    else:
        print("El valor mínimo registrado para el mínimo de nochess fue el mismo en ambas ciudades.")
    
    if max_df1 > max_df2:
        print(f"El valor máximo para el mínimo de noches en Praga es mayor, la diferencia fue de {dif_max} noches mas en comparación a CDMX.")
    elif max_df1 < max_df2:
        print(f"El valor máximo para el mínimo de noches en CDMX es mayor, la diferencia fue de {dif_max} noches mas en comparación a Praga.")
    else:
        print("El valor máximo registrado para el mínimo de noches fue el mismo en ambas ciudades.")
        
def maximo():
    #Precio
    CDMXLimpio = pd.read_csv("CDMXLimpio.csv")
    PragueLimpio = pd.read_csv("PragueLimpio.csv")
    media_df1 = PragueLimpio['maximum_nights'].mean()
    media_df2 = CDMXLimpio['maximum_nights'].mean()
    mediana_df1= PragueLimpio['maximum_nights'].median()
    mediana_df2 = CDMXLimpio['maximum_nights'].median()
    moda_df1=PragueLimpio['maximum_nights'].mode()
    moda_df2=CDMXLimpio['maximum_nights'].mode()
    min_df1=PragueLimpio['maximum_nights'].min()
    min_df2=CDMXLimpio['maximum_nights'].min()
    max_df1=PragueLimpio['maximum_nights'].max()
    max_df2=CDMXLimpio['maximum_nights'].max()
    
    # Calcular la diferencia numérica entre las medias
    dif_media = round(abs(media_df1 - media_df2),2)
    dif_mediana = round(abs(mediana_df1 - mediana_df2),2)
    dif_mode = round(abs(moda_df1 - moda_df2),2)
    dif_min = round(abs(min_df1 - min_df2),2)
    dif_max = round(abs(max_df1 - max_df2),2)
   
    
    
    
    print("\nAnálisis del máximo de noches en la ciudad de Praga.")
    print(f"El promedio de máximoo de noches en Praga es de {round(media_df1,2)}.")
    print(f"El valor de la mediana en Praga es de {round( mediana_df1,2)}.")
    print(f"El valor(es) modal(es) en Praga es(son) de {round( moda_df1,2)}.")
    print(f"El valor minimo en la ciudad de Praga es de {( min_df1)}.")
    print(f"El valor máximo en la ciudad de Praga es de {round( max_df1,2)}.")
    
    print("\nAnálisis del mínimo de noches en la CDMX")
    print(f"El promedio de máximo de noches en CDMX es de {round(media_df2,2)}.")
    print(f"El valor de la mediana en CDMX es de {round( mediana_df2,2)}.")
    print(f"El valor(es) modal(es) en CDMX es(son) de {round( moda_df2,2)}.")
    print(f"El valor minimo en la ciudad de CDMX es de {( min_df2)}.")
    print(f"El valor máximo en la ciudad de CDMX es de {round( max_df2,2)}.")    
    
    
    print('\nComparación de las ciudades')
    if media_df1 > media_df2:
        print(f"La media de máximo de noches en Praga es mayor, la diferencia es de {dif_media} noches en comparación a CDMX.")
    elif media_df1 < media_df2:
        print(f"La media de máximo de noches en CDMX es mayor, la diferencia es de {dif_media} noches en comparación a Praga.")
    else:
        print("El promedio de máximo de noches es el mismo para ambas ciudades.")
        

    if mediana_df1 > mediana_df2:
        print(f"El valor de la mediana para el máximo de noches en Praga es mayor, la diferencia es de {dif_mediana} noches en comparación a CDMX.")
    elif mediana_df1 < mediana_df2:
        print(f"El valor de la mediana para el máximo de noches en CDMX es mayor, la diferencia es de {dif_mediana} noches en comparación a Praga.")
    else:
        print("El valor de la mediana para el máximo de noches es el mismo en ambas ciudades.")
        
        
    if min_df1 > min_df2:
        print(f"El valor mínimo para el máximo de noches en Praga fue mayor, la diferencia fue de {dif_min} noches mas en comparación a CDMX.")
    elif min_df1 < min_df2:
        print(f"El valor mínimo para el máximo de noches en CDMX fue mayor, la diferencia fue de {dif_min} noches mas en comparación a Praga.")
    else:
        print("El valor mínimo registrado para el máximo de noches fue el mismo en ambas ciudades.")
    
    if max_df1 > max_df2:
        print(f"El valor máximo para el máximo de noches en Praga es mayor, la diferencia fue de {dif_max} noches mas en comparación a CDMX.")
    elif max_df1 < max_df2:
        print(f"El valor máximo para el máximo de noches en CDMX es mayor, la diferencia fue de {dif_max} noches mas en comparación a Praga.")
    else:
        print("El valor máximo registrado para el máximo de noches fue el mismo en ambas ciudades.")
        

def reviews():
    #Precio
    CDMXLimpio = pd.read_csv("CDMXLimpio.csv")
    PragueLimpio = pd.read_csv("PragueLimpio.csv")
    media_df1 = PragueLimpio['reviews_per_month'].mean()
    media_df2 = CDMXLimpio['reviews_per_month'].mean()
    mediana_df1= PragueLimpio['reviews_per_month'].median()
    mediana_df2 = CDMXLimpio['reviews_per_month'].median()
    moda_df1=PragueLimpio['reviews_per_month'].mode()
    moda_df2=CDMXLimpio['reviews_per_month'].mode()
    min_df1=PragueLimpio['reviews_per_month'].min()
    min_df2=CDMXLimpio['reviews_per_month'].min()
    max_df1=PragueLimpio['reviews_per_month'].max()
    max_df2=CDMXLimpio['reviews_per_month'].max()
    
    # Calcular la diferencia numérica entre las medias
    dif_media = round(abs(media_df1 - media_df2),2)
    dif_mediana = round(abs(mediana_df1 - mediana_df2),2)
    dif_mode = round(abs(moda_df1 - moda_df2),2)
    dif_min = round(abs(min_df1 - min_df2),2)
    dif_max = round(abs(max_df1 - max_df2),2)
   
    
    
    
    print("\nAnálisis de reviews en plataforma asignado por los usuarios  en la ciudad de Praga.")
    print(f"El promedio de reviews en Praga es de {round(media_df1,2)}.")
    print(f"El valor de la mediana en Praga es de {round( mediana_df1,2)}.")
    print(f"El valor(es) modal(es) en Praga es(son) de {round( moda_df1,2)}.")
    print(f"El valor minimo en la ciudad de Praga es de {( min_df1)}.")
    print(f"El valor máximo en la ciudad de Praga es de {round( max_df1,2)}.")
    
    print("\nAnálisis de reviews en plataforma asignado por los usuarios en la CDMX")
    print(f"El promedio de reviews en CDMX es de {round(media_df2,2)}.")
    print(f"El valor de la mediana en CDMX es de {round( mediana_df2,2)}.")
    print(f"El valor(es) modal(es) en CDMX es(son) de {round( moda_df2,2)}.")
    print(f"El valor minimo en la ciudad de CDMX es de {( min_df2)}.")
    print(f"El valor máximo en la ciudad de CDMX es de {round( max_df2,2)}.")    
    
    
    print('\nComparación de las ciudades')
    if media_df1 > media_df2:
        print(f"La media de reviews en Praga es mayor, la diferencia es de {dif_media} reviewsen comparación a CDMX.")
    elif media_df1 < media_df2:
        print(f"La media de reviews en CDMX es mayor, la diferencia fue de {dif_media} reviews en comparación a Praga.")
    else:
        print("El promedio de reviews es el mismo para ambas ciudades.")
        

    if mediana_df1 > mediana_df2:
        print(f"El valor de la mediana en reviews en Praga es mayor, la diferencia es de {dif_mediana} reviews en comparación a CDMX.")
    elif mediana_df1 < mediana_df2:
        print(f"El valor de la mediana en reviews en CDMX es mayor, la diferencia es de {dif_mediana} reviews en comparación a Praga.")
    else:
        print("El valor de la mediana en reviews es el mismo en ambas ciudades.")
        
        
    if min_df1 > min_df2:
        print(f"El valor mínimo de reviews en Praga fue mayor, la diferencia fue de {dif_min} reviews mas en comparación a CDMX.")
    elif min_df1 < min_df2:
        print(f"El valor mínimo de reviews en CDMX fue mayor, la diferencia fue de {dif_min} reviews mas en comparación a Praga.")
    else:
        print("El valor mínimo registrado de reviews fue el mismo en ambas ciudades.")
    
    if max_df1 > max_df2:
        print(f"El valor máximo de reviews en Praga es mayor, la diferencia fue de {dif_max} reviews mas en comparación a CDMX.")
    elif max_df1 < max_df2:
        print(f"El valor máximo de reviews en CDMX es mayor, la diferencia fue de {dif_max} reviews mas en comparación a Praga.")
    else:
        print("El valor máximo registrado de reviews fue el mismo en ambas ciudades.")