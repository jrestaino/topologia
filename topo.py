import json
import os


def limpioNumerCaracteres(numeroIn):
    numeroIn = numeroIn.rstrip('\r\n')
    numeroIn = numeroIn.replace('{','')
    numeroIn = numeroIn.replace('}','')
    return numeroIn

def encontrar_parejas_adyacentes(directirioIn):
    #parejas_adyacentes = []

    # Obtiene una lista de todos los archivos en el directorio
    archivosIn = os.listdir(directirioIn)

    # Recorre la lista de archivos
    for archivoIn in archivosIn:

        # inicializo los adyacentes
        parejas_adyacentes = []
        # Verifica si es un archivo (no un directorio)
        if os.path.isfile(os.path.join(directirioIn, archivoIn)):

            # Archivo a procesar
            print(archivoIn)
            archivo = directirioIn + archivoIn
            with open(archivo, 'r') as f:

                # Recorro el archivo
                for asPath in f:

                    # Corrijo los ASPATH del tipo "ASPATH: 61573 6762 2914 23033 {9002,27323,45147,58381,138074}"
                    asPath = asPath.strip('{}')
                    asPath = asPath.replace(',', ' ')

                    # Obtener los números de la línea (no leo el primer elemento que siempre es AS-PATH)
                    numeros = asPath.split()[1:]  
                    
                    # Recorrer los números de la línea
                    for i in range(len(numeros) - 1):

                        numeros[i] = limpioNumerCaracteres(numeros[i])
                        numeros[i + 1] = limpioNumerCaracteres(numeros[i + 1])
                        intNumeroI = int(numeros[i])
                        try:
                            intNumeroII = int(numeros[i + 1])
                        except ValueError:
                            print("asPath: " + str(asPath))
                            print("numeros: " + str(numeros))
                            print('i: ' + str(i))
                            print('numeros[i]: ' + str(numeros[i]))
                            print('numeros[i + 1]: ' + str(numeros[i + 1]))
                        

                        # comparo cual es menor, casteo a int por que sino el resultado no es el correcto
                        # como solo almaceno si los adjuntos son deferentes el append al conjunto lo realizo dentro del if
                        if intNumeroI < intNumeroII:
                            pareja_adyacente = numeros[i] + "," + numeros[i + 1]
                            parejas_adyacentes.append(pareja_adyacente)

                        elif intNumeroI < intNumeroII:
                            pareja_adyacente = numeros[i + 1] + "," + numeros[i]
                            parejas_adyacentes.append(pareja_adyacente)
                        

            # Eliminar duplicados de la lista
            parejas_adyacentes = list(set(parejas_adyacentes))
            print(len(parejas_adyacentes))

            archivoSalida = 'resultados/resultado_' + archivoIn + '.json'
            # Guardar el resultado en un archivo JSON
            with open(archivoSalida, "w") as archivo:
                json.dump(parejas_adyacentes, archivo)

directorioIn = 'archivosBgpDump/'

encontrar_parejas_adyacentes(directorioIn)
