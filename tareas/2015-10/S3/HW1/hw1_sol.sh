#!/bin/bash
# Solución del primer taller del curso Herramientas Computacionales
# 27-Jan-2015

# parte a
#echo "*****Parte a*****"
wget https://github.com/spsaaibi/ComputationalToolsData/raw/master/data/HYG/hyg.tar.gz
tar -zxvf hyg.tar.gz
rm hyg.tar.gz

# parte b
# Una alternativa sería usar awk con una condicional sobre el campo de interés.
echo "*****Parte b*****"
echo "Regulus"
grep "Regulus" hyg.csv

# parte c
echo "*****Parte c*****"
stars=$(cat hyg.csv | wc -l)
# Las primeras 32 líneas no son entradas del catálogo, contienen información auxiliar.
stars=$((stars-32))
echo "La base de datos tiene $stars estrellas."

# parte d
echo "*****Parte d*****"
echo "Número de líneas: $(cat hyg.csv | wc -l)"
echo "Número de palabras: $(cat hyg.csv | wc -w)"
echo "Número de bytes: $(cat hyg.csv | wc -c)"

# parte e
echo "*****Parte e*****"
# La columna 16 tiene la información relevante, sed al final para eliminar espacios en blanco, opción -F "," para instruir a awk que la coma es el separador de columnas.
printf "Cantidad de estrellas de tipo espectral G2: "
awk -F "," '$16=="G2" {print $1}' hyg.csv | wc -l | sed 's/ //g'

# parte f
# Se construye el archivo requerido en dos etapas,
# primero se ponen las primeras 32 líneas
# y luego usando >> se alimentan el resto de ellas.
echo "*****Parte f*****"
head -32 hyg.csv > EstrellasG2.csv
awk -F "," '$16=="G2"' hyg.csv >> EstrellasG2.csv

# parte g
echo "*****Parte g*****"
# La columna 10 tiene la información sobre distancia
awk -F "," '$10>10 && $10<50 && $16=="G2V"' hyg.csv > EstrellasG2_10-50_ly.csv

# parte h
# No olvidar que en sed ^ representa el inicio de línea y $ el final.
echo "*****Parte h*****"
sed 's/^/estrellas especiales,/g' EstrellasG2_10-50_ly.csv | sed 's/$/,enero-2015/g' > EstrellasG2_10-50_ly_ng.csv

# parte i
echo "*****Parte i*****"
tar -zcvf EstrellasG2_10-50_ly_ng.tar.gz EstrellasG2_10-50_ly_ng.csv

