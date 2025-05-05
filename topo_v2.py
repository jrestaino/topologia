import json
import os


def limpioNumerCaracteres(numeroIn):
    numeroIn = numeroIn.rstrip('\r\n')
    numeroIn = numeroIn.replace('{', '')
    numeroIn = numeroIn.replace('}', '')
    return numeroIn


def encontrar_parejas_adyacentes(directorioIn):
    # Obtiene una lista de todos los archivos en el directorio
    archivosIn = os.listdir(directorioIn)

    for archivoIn in archivosIn:
        # Usamos un conjunto para evitar duplicados y reducir uso de RAM
        parejas_adyacentes = set()

        # Verifica si es un archivo (no un directorio)
        if os.path.isfile(os.path.join(directorioIn, archivoIn)):
            print(f"Procesando: {archivoIn}")
            archivo = os.path.join(directorioIn, archivoIn)

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
                        try:
                            num1 = limpioNumerCaracteres(numeros[i])
                            num2 = limpioNumerCaracteres(numeros[i + 1])

                            intNum1 = int(num1)
                            intNum2 = int(num2)

                            # Ordenamos para evitar duplicados tipo 100,200 y 200,100
                            pareja = ",".join(sorted([num1, num2], key=int))
                            parejas_adyacentes.add(pareja)

                        except ValueError:
                            print("Error al convertir a entero:")
                            print("asPath:", asPath)
                            print("numeros:", numeros)
                            print("i:", i)
                            print("num1:", numeros[i])
                            print("num2:", numeros[i + 1])

            print(f"Total de parejas únicas: {len(parejas_adyacentes)}")

            archivoSalida = os.path.join('resultados', f'resultado_{archivoIn}.json')
            os.makedirs('resultados', exist_ok=True)

            with open(archivoSalida, "w") as archivo_out:
                json.dump(sorted(parejas_adyacentes), archivo_out)


directorioIn = 'archivosBgpDump/'
encontrar_parejas_adyacentes(directorioIn)
