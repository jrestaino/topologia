import json
import os

def levantoJson(paramArchivoJson):
    with open(paramArchivoJson, "r") as archivo:
        listaArchivo = json.load(archivo)
        return listaArchivo
'''
archivoRrc03 = 'resultados/resultado_rrc_03_bview_20230501_0000.txt.json'
archivoRrc00 = 'resultados/resultado_rrc_00_bview_20230501_0000.txt.json'

listRrc03 = levantoJson(archivoRrc03)
listRrc00 = levantoJson(archivoRrc00)

print(len(listRrc03))
print(len(listRrc00))
orListas = list( set(listRrc03) | set(listRrc00) )
print(len(orListas))
'''

directorioIn = 'resultados/'
topologiaFinal = []

# Obtiene una lista de todos los archivos en el directorio
archivosIn = os.listdir(directorioIn)
# Recorre la lista de archivos
for archivoIn in archivosIn:

    # Verifica si es un archivo (no un directorio)
    if os.path.isfile(os.path.join(directorioIn, archivoIn)):

        archivoRrc = 'resultados/' + archivoIn
        # Archivo a procesar
        print(archivoRrc)
        listRrcArchivoIn = levantoJson(archivoRrc)
        print('len Archivo RRC: ' + str(len(listRrcArchivoIn)))
        topologiaFinal = list( set(topologiaFinal) | set(listRrcArchivoIn) )
        print('len topologiaFinal: ' + str(len(topologiaFinal)))

print('len toplogiaFinal al final:' + str(len(topologiaFinal)))

archivoSalidaTopoCompilado = 'topoTotal.json'
with open(archivoSalidaTopoCompilado, 'w') as archivoSalidaTopoCompiladoJson:
    # Escribir el diccionario en el archivo en formato JSON
    json.dump(topologiaFinal, archivoSalidaTopoCompiladoJson)