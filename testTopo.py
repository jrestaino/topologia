def limpioNumerCaracteres(numeroIn):
    numeroIn
    numeroIn = numeroIn.rstrip('\r\n')
    numeroIn = numeroIn.replace('{','')
    numeroIn = numeroIn.replace('}','')
    return numeroIn


def encontrar_parejas_adyacentes(lineas):
    parejas_adyacentes = []

    for linea in lineas:
        print(linea)
        linea = linea.strip('{}')
        linea = linea.replace(',', ' ')

        numeros = linea.split()[1:]  # Obtener los números de la línea
        print('numeros: ' + str(numeros))

        print('len - 1: ' + str(len(numeros) - 1))

        # Recorrer los números de la línea
        for i in range(len(numeros) - 1):
            print('i: ' + str(i))

            numeros[i] = limpioNumerCaracteres(numeros[i])
            numeros[i + 1] = limpioNumerCaracteres(numeros[i + 1])

            print('numeros[i]: ' + str(numeros[i]))
            print('numeros[i + 1]: ' + str(numeros[i + 1]))

            if int(numeros[i]) < int(numeros[i + 1]):
                print('i < i+1')
                pareja_adyacente = str(numeros[i]) + "," + str(numeros[i + 1])
                print('pareja_adyacente: ' + pareja_adyacente)
                parejas_adyacentes.append(pareja_adyacente)
            elif int(numeros[i + 1]) < int(numeros[i]):
                print('i+1 < i')
                pareja_adyacente = str(numeros[i + 1]) + "," + str(numeros[i])
                print('pareja_adyacente: ' + pareja_adyacente)
                parejas_adyacentes.append(pareja_adyacente)


    # Eliminar duplicados de la lista
    parejas_adyacentes = list(set(parejas_adyacentes))

    return parejas_adyacentes

# Ejemplo de uso
entradas = [
    "ASPATH: 46997 201106 201106 50131 36236 2914 3356 749",
    "ASPATH: 263702 3356 7018",
    "ASPATH: 14840 7018 3356",
    "ASPATH: 61573 6762 2914 23033 {9002,27323,45147,58381,138074}"
]

resultado = encontrar_parejas_adyacentes(entradas)
for pareja in resultado:
    print(pareja)
