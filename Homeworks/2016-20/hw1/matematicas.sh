#!/bin/bash 

wget https://raw.githubusercontent.com/ComputoCienciasUniandes/HerramientasComputacionalesDatos/master/Homework/hw1/01_notas.tsv

awk '{if($3=="MATEMA" && ($4+$5+$6)>=9) print $0}' 01_notas.tsv | wc | awk '{print $1}' > pasaron.txt

# El primer comando, wget seguido de la direccion URL, descarga el archivo del repositorio del curso a nuestro directorio de trabajo.
# Seguido podemos usar simplemente awk para juzgar ambas condiciones, gracias a que nuestro texto esta apropiadamente formateado en 
# columnas. La primera parte del comando, a saber "awk '{if($3=="MATEMA" && ($4+$5+$6)>=9) print $0}' 01_notas.tsv" selecciona tanto 
# los estudiantes de matematicas como los que pasaron la materia. Note que la condicion de la carrera, como esta comparando caracteres,
# necesita estar entre comillas. Tambien que si la suma de las columnas 4, 5 y 6 es mayor a 9, es equivalente a que el promedio o
# nota final sea mayor a tres, es decir a que haya pasado el curso. Asi, las lineas que cumplan esas condiciones seran re-escritas
# usando la salida estandaro terminal, pero haciendo piping, " | ", podemos conectar la salida estandar de awk con la entrada estandar
# de wc, lo que ahora produciria una sola linea cuya primera columna sera el numero de filas para la anterior salida de awk, la 
# segunda el numero de palabras y la tercera el numero de caracteres. Despues podriamos conectar de nuevo salida estandar de wc con 
# entrada estandar de awk y seleccionar la primera columna, que corresponde finalmente al numero de personas de la carrera de 
# matematicas que pasaron el curso. Finalmente se redirige la salida de awk a un archivo de texto llamado "pasaron.txt", que tendra
# entonces solo ese numero. Similarmente se podria haber hecho usando varias lineas de codigo usando archivos intermedios, asi:

awk '{if(($4+$5+$6)/3 >= 3) print $3}' 01_notas.tsv > pasaron_todas_las_carreras.txt
awk '{if($1=="MATEMA") print $0}' pasaron_todas_las_carreras.txt > de_matematicas.txt
wc de_matematicas.txt > cifras.txt
awk '{print $1}' cifras.txt > pasaron1.txt
