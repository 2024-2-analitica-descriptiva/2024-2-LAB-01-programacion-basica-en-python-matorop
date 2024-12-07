"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import itertools

def pregunta_09():
        with open("files/input/data.csv",'r') as f:
             l=[row.split("\t")[4].replace("\n","").split(",") for row in f.readlines()]
             l=[row.split(":")[0] for row in list(itertools.chain(*l))]
             l=sorted([(row, l.count(row)) for row in set(l)])

        
        return dict(l)

if __name__ =="__main__":
    print(pregunta_09())




    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
