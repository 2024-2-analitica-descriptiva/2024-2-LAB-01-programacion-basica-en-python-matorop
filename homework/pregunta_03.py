"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    with open("files/input/data.csv",'r') as f:
        l=[row.split("\t")[:2] for row in f.readlines()]
    
    cont= {
        key: sum(int(value) for k, value in l if k == key)
        for key in set(k for k, _ in l)
    }

    return sorted(list(cont.items()))


if __name__ =="__main__":
    print(pregunta_03())
    

    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
