#!/bin/bash 

wget https://raw.githubusercontent.com/ComputoCienciasUniandes/HerramientasComputacionalesDatos/master/Homework/hw1/01_notas.tsv

awk '{if($3=="MATEMA" && ($4+$5+$6)>=9) print $0}' 01_notas.tsv | wc | awk '{print $1}' > pasaron.txt

# El primer comando, wget seguido de la direccion URL, descarga el archivo del repositorio del curso a nuestro directorio de trabajo.
# Seguido podemos usar simplemente awk para juzgar ambas condiciones, gracias a que nuestro texto esta apropiadamente formateado en columnas.
