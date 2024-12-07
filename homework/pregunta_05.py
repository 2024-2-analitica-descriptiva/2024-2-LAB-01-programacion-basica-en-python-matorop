"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    
    with open("files/input/data.csv",'r') as f:
        l=[row.split("\t")[:2] for row in f.readlines()]
    
    minmax=[
        (
             key,
            max(int(value) for k, value in l if k == key),
            min(int(value) for k, value in l if k == key),
        )
        for key in set(k for k, _ in l)
    ]
    
    return sorted(minmax)

if __name__ =="__main__":
    print(pregunta_05())

    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
