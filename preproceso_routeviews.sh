#!/bin/bash

mkdir -p procesados

echo "==> Iniciando procesamiento de archivos RIB..."

while IFS= read -r linea; do
    # Extraer colector y archivo
    colector=$(echo "$linea" | cut -d' ' -f1)
    archivo_original=$(echo "$linea" | cut -d' ' -f2)

    echo ""
    echo "==> Procesando colector: $colector"
    echo "    Archivo: $archivo_original"

    # Renombrar temporalmente
    echo "    Copiando archivo para descompresión..."
    cp "$archivo_original" rib.20250401.0000.bz2

    # Descomprimir
    echo "    Descomprimiendo..."
    bunzip2 -f rib.20250401.0000.bz2

    # Procesar con bgpdump y filtrar ASPATH sin comas
    echo "    Ejecutando bgpdump..."
    bgpdump rib.20250401.0000 | grep ASPATH | grep -v , > "procesados/${colector}_20250401"

    echo "    Archivo procesado guardado en: procesados/${colector}_20250401"

    # Limpiar temporal
    echo "    Eliminando archivo temporal..."
    rm -f rib.20250401.0000

done < archivosColectorRV.txt

echo ""
echo "==> Procesamiento completado."
