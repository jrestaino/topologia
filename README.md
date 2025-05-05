# Topologia
Codigo para determinar como estan interconectados los AS a partir de archivos MRT

# Scirpts de trabajo

**topo_v2.py** Analiza los archivos de entrada y genera la información topologica a partir de cada uno de ellos
**compilodatosTopo** Compila resultados obtenidos en topo.py generando un archivo solo con toda la topología visualizada

# Archivos de entrada
Se deben de agregar en el directorio archivosBgpDump todos los archivos dump MRT con lineas de ASPATH.
A modo de ejemplo:

```
archivosBgpDump$ more rrc_00_bview_20230501_0000.txt | head
ASPATH: 37721 6762
ASPATH: 44393 50892
ASPATH: 44393 50892
ASPATH: 55720
ASPATH: 50628
ASPATH: 34927
ASPATH: 35708
ASPATH: 44103 1299
ASPATH: 47422
ASPATH: 34854 1299
```

En una prinera instancia (esta a agregar en una segunda versión) se deben de quitar los ASPATH con AS agregados, estos son los que tienen líneas con llaves { }. En una segunda versión voy a eliminarlas desde el script, pero estos ASPATH deben de eliminarse ya que no se sabe si los miemboros dentro de las llaves son vecinos.

# Script topo_v2.py

Este script toma todos los archivos de archivosBgpDump/ con el formato explicado en #Archivos de entrada#, analiza cada uno de los archivos y por cada uno de los archivos genera un archivo .json que tiene todos los AS que aparecen de forma consecutiva en el ASPATH (no considerando cuando el AS esta repetido) y los forma en parejas poniendo el menor primero.

A modo de ejemplo si un archivo llamado **resultado_rrc_00_bview_20230501_0000.txt** tuviera las entradas
```
ASPATH 131464 136991
ASPATH 115000 136991
ASPATH 150022 45117
ASPATH 1257 1257
```
Obtendríamos como salida en la carpeta **resultados/** un archivo **resultado_rrc_00_bview_20230501_0000.txt.json** con el siguiente formato

["131464,136991", "115000,136991", "45117,150022", "1257,48657"]

```
$ ls -hlrt resultados/
total 43M
-rw-rw-r-- 1 uai uai 1,9M jul 12  2023 resultado_rrc_04_bview_20230501_0000.txt.json
-rw-rw-r-- 1 uai uai 1,5M jul 12  2023 resultado_rrc_18_bview_20230501_0000.txt.json
-rw-rw-r-- 1 uai uai 2,5M jul 12  2023 resultado_rrc_00_bview_20230501_0000.txt.json
-rw-rw-r-- 1 uai uai 2,0M jul 12  2023 resultado_rrc_07_bview_20230501_0000.txt.json
-rw-rw-r-- 1 uai uai 2,6M jul 12  2023 resultado_rrc_25_bview_20230501_0000.txt.json
-rw-rw-r-- 1 uai uai 2,6M jul 12  2023 resultado_rrc_12_bview_20230501_0000.txt.json
-rw-rw-r-- 1 uai uai 2,1M jul 12  2023 resultado_rrc_10_bview_20230501_0000.txt.json
-rw-rw-r-- 1 uai uai 1,8M jul 12  2023 resultado_rrc_26_bview_20230501_0000.txt.json
-rw-rw-r-- 1 uai uai 2,0M jul 12  2023 resultado_rrc_05_bview_20230501_0000.txt.json
-rw-rw-r-- 1 uai uai 2,1M jul 12  2023 resultado_rrc_24_bview_20230501_0000.txt.json
-rw-rw-r-- 1 uai uai 2,0M jul 12  2023 resultado_rrc_13_bview_20230501_0000.txt.json
-rw-rw-r-- 1 uai uai 2,0M jul 12  2023 resultado_rrc_11_bview_20230501_0000.txt.json
-rw-rw-r-- 1 uai uai 2,2M jul 12  2023 resultado_rrc_20_bview_20230501_0000.txt.json
-rw-rw-r-- 1 uai uai 1,7M jul 12  2023 resultado_rrc_16_bview_20230501_0000.txt.json
-rw-rw-r-- 1 uai uai 2,0M jul 12  2023 resultado_rrc_23_bview_20230501_0000.txt.json
-rw-rw-r-- 1 uai uai 1,8M jul 12  2023 resultado_rrc_06_bview_20230501_0000.txt.json
-rw-rw-r-- 1 uai uai 2,6M jul 12  2023 resultado_rrc_03_bview_20230501_0000.txt.json
-rw-rw-r-- 1 uai uai 2,3M jul 12  2023 resultado_rrc_21_bview_20230501_0000.txt.json
-rw-rw-r-- 1 uai uai 1,9M jul 12  2023 resultado_rrc_14_bview_20230501_0000.txt.json
-rw-rw-r-- 1 uai uai 2,7M jul 12  2023 resultado_rrc_15_bview_20230501_0000.txt.json
-rw-rw-r-- 1 uai uai 1,8M jul 12  2023 resultado_rrc_22_bview_20230501_0000.txt.json
```
# Script compiloDatosTopo.py

El scirpt compiloDatosTopo.py, va a levantar todos los archivos de la carpeta resultados/ y va a compilar los datos de los mismos.

El scrpit lo que hace es un or entre todos los json obtenidos previamente y deja el resultado en **topoTotal.json**

# Script buscoParesTopo.py

Este script sivre para debug, con el mismo se buscan pares dentro de un json de salida de una topología

Ejemplo
python buscoParesTopo.py resultados/resultado_rrc12_20250401.json 35,3356
