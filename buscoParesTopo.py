# -*- coding: utf-8 -*-

import json
import sys

if len(sys.argv) != 3:
    print("Uso: python analizoTopo.py <archivo.json> <pareja>")
    print("Ejemplo: python analizoTopo.py datos.json 6881,43542")
    sys.exit(1)

ruta_archivo = sys.argv[1]
elemento_a_buscar = sys.argv[2]

# Leer el archivo JSON
with open(ruta_archivo, 'r') as archivo:
    lista = json.load(archivo)

# Buscar el elemento
if elemento_a_buscar in lista:
    print('El elemento "{}" fue encontrado.'.format(elemento_a_buscar))
else:
    print('El elemento "{}" NO fue encontrado.'.format(elemento_a_buscar))
