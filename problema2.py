
fichero = input("Introduce el nombre del fichero: ")

with open(f'{fichero.split(".")[0]}.txt', 'r') as f:
    palabras = {}
    for line in f:
        for palabra in line.split():
            palabra = palabra.strip(".,;!¡?-").lower()
            if palabra in palabras:
                palabras[palabra] += 1
            else:
                palabras[palabra] = 1

    for palabra, cantidad in sorted(palabras.items()):
        print(f"{palabra}: {cantidad}")