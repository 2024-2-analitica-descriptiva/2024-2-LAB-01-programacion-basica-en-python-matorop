"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def contar_registros(lista):
    contador = {}
    for item in lista:
        if item in contador:
            contador[item] += 1
        else:
            contador[item] = 1
    # Convierte el diccionario en una lista de tuplas y ordénalas alfabéticamente
    resultado = sorted(contador.items())
    return resultado

def pregunta_02():
    contador={}
    with open('files/input/data.csv', 'r') as f:
        l = [str(row.split("\t")[0]) for row in f.readlines()]  # Suponiendo que el separador es un tabulador
        
        
        # Contar registros e imprimirlos como tuplas
        resultado = contar_registros(l)
        return(resultado)

if __name__ == "__main__":
    print(pregunta_02())

    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """