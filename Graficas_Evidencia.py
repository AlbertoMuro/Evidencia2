import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def pastel ():
    df = pd.read_csv("CDMXLimpio.csv")
    print(df)

    dfp = pd.read_csv("PragueLimpio.csv")
    print(dfp)
    plt.subplot(211)
    #fig = plt.figure(figsize = ( 5,3 ))
    df['host_response_time'].value_counts().plot(kind='pie',autopct='%1.2f%%')
    plt.title("Tiempo de respuesta Mexico")

    plt.subplot(212)
    #fig = plt.figure(figsize = ( 5,3 ))
    dfp['host_response_time'].value_counts().plot(kind='pie',autopct='%1.2f%%')
    plt.title("Tiempo de respuesta Praga")
    plt.show()

def barras (df, dfp):
    plt.subplot(211)
    #fig = plt.figure(figsize = ( 5,3 ))
    df3=df['property_type'].value_counts()
    df4=df3.head(10)
    print(df4)
    print(type(df4))
    df4.plot.bar(title="Tipo de propiedad Mexico",color="g")

    plt.subplot(212)
    #fig = plt.figure(figsize = ( 5,3 ))
    dfp3=dfp['property_type'].value_counts()
    dfp4=dfp3.head(10)
    print(dfp4)
    print(type(dfp4))
    dfp4.plot.bar(title="Tipo de propiedad Praga",color="r")
    plt.show()


def hist(df, dfp): 
    plt.subplot(221)
    df5=df[df['price']<5000]
    print(type(df5))
    print(df5.columns)

    plt.hist(df5['price'],bins=20,color="g")
    plt.title("Precio Mexico")


    plt.subplot(222)
    dfp5=dfp[dfp['price']<5000]
    print(type(dfp5))
    print(dfp5.columns)

    plt.hist(dfp5['price'],bins=20,color="r")
    plt.title("Precio Praga")
    plt.show()

def boxplot(df, dfp): 
    plt.subplot(223)
    df5=df[df['review_scores_rating']>4]
    plt.boxplot(df5['review_scores_rating'],vert=0)
    plt.title("Calificacion Mexico")

    plt.subplot(224)
    dfp5=dfp[dfp['review_scores_rating']>4]
    plt.boxplot(dfp5['review_scores_rating'],vert=0)
    plt.title("Calificacion Praga")

    plt.show()

# def main():
#     # df = pd.read_csv("CDMXLimpio.csv")
#     # print(df)

#     # dfp = pd.read_csv("PragueLimpio.csv")
#     # print(dfp)

#     pastel()    
#     plt.show()  

#     # barras()    
#     # plt.show()  

#     # hist()      
#     # plt.show()  

#     # boxplot()   
#     # plt.show()  

# if __name__ == "__main__":
#     main()