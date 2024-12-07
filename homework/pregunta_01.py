"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    with open('files/input/data.csv', 'r') as f:
        l=[int(row.split("\t")[1]) for row in f.readlines()]
        print(l)
        return sum(l)




if __name__ == "__main__":
    print(pregunta_01())
    
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
