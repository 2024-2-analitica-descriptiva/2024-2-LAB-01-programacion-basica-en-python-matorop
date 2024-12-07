"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import itertools

def pregunta_11():
    with open("files/input/data.csv",'r') as f:
        l=[[int(row.split("\t")[1])] + [row.split("\t")[3]] for row in f.readlines()]
    l= [[char, item[0]] for item in l for char in item[1].split(",")]

    cont={
        key: sum(int(value) for k, value in l if k == key)
        for key in set(k for k, _ in l)
    }

    return dict(sorted(cont.items()))

if __name__ =="__main__":
    print(pregunta_11())

    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
