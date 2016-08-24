#!/bin/bash 

wget https://raw.githubusercontent.com/ComputoCienciasUniandes/HerramientasComputacionalesDatos/master/Homework/hw1/01_notas.tsv

awk '{if($3=="MATEMA" && ($4+$5+$6)>=9) print $0}' 01_notas.tsv | wc | awk '{print $1}' > pasaron.txt

# El primer comando, wget seguido de la direccion URL, descarga el archivo del repositorio del curso a nuestro directorio de trabajo.
# Seguido podemos usar simplemente awk para juzgar ambas condiciones, gracias a que nuestro texto esta apropiadamente formateado en 
# columnas. La primera parte del comando, a saber "awk '{if($3=="MATEMA" && ($4+$5+$6)>=9) print $0}' 01_notas.tsv" selecciona tanto 
# los estudiantes de matematicas como los que pasaron la materia. Note que la condicion de la carrera, como esta comparando caracteres,
# necesita estar entre comillas. Tambien que si la suma de las columnas 4, 5 y 6 es mayor a 9, es equivalente a que el promedio o
# nota 
