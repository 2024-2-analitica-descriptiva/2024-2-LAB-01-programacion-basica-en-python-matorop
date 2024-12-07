"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    with open("files/input/data.csv",'r') as f:
        l=[[row.split("\t")[0]]+ row.split("\t")[3:] for row in f.readlines()]

        cont=[
            (
                item[0],
                len(item[1].split(",")),
                len(item[2].split(",")), 
            )
            for item in l
        ]

    return (cont)

if __name__ =="__main__":
    print(pregunta_10())

    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
