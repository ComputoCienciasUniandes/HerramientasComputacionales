wget https://raw.githubusercontent.com/ComputoCienciasUniandes/MetodosComputacionalesDatos/master/homework/2014-20/hw_1/notas_fisicaII_201320.dat

echo "1."
awk '{if($1 >= 60) print $0}' notas_fisicaII_201320.dat | wc -l
echo -e "estudiantes ganaron el primer parcial.\n"
awk '{if($2 >= 60) print $0}' notas_fisicaII_201320.dat | wc -l
echo -e "estudiantes ganaron el segundo parcial.\n"
awk '{if($3 >= 60) print $0}' notas_fisicaII_201320.dat | wc -l
echo -e "estudiantes ganaron el tercer parcial.\n"

echo "2."
awk '{if($6>=60 && (($1<60 && $2>=60 && $3>=60) || ($2<60 && $1>=60 && $3>=60) || ($3<60 && $1>=60 && $2>=60))) print $0}' notas_fisicaII_201320.dat | wc -l
echo -e "estudiantes perdieron exactamente un parcial y ganaron la materia.\n"

rm notas_fisicaII_201320.dat
