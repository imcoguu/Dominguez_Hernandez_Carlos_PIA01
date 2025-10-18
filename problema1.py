
def procesar_lista(lista):
    return sorted({x for x in lista if x >= 0})

lista = [4, -1, 2, 4, 3, -5, 2]
print(procesar_lista(lista))