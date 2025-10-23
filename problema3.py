
def analizar_listas(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    interseccion = conjunto1.intersection(conjunto2)
    union = conjunto1.union(conjunto2)
    diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)

    return {
        'interseccion': interseccion,
        'union': union,
        'diferencia_simetrica': diferencia_simetrica
    }


lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
resultado = analizar_listas(lista1, lista2)
print(f"Intersección: {resultado['interseccion']}")
print(f"Unión: {resultado['union']}")
print(f"Diferencia Simétrica: {resultado['diferencia_simetrica']}")
