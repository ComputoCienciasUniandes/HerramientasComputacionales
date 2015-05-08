wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt

echo "Veces que aparece la vocal 'a':
"

grep -o -i "a" metamorphosis.txt > data1.txt

wc -l  data1.txt

wc -l data1.txt > dataametamorphosis.txt

echo "
"

echo "Veces que aparece la vocal 'e':
"

grep -o -i "e" metamorphosis.txt > data2.txt

wc -l  data2.txt

echo "
"

echo "Veces que aparece la vocal 'i':
"

grep -o -i "i" metamorphosis.txt > data3.txt

wc -l  data3.txt

echo "
"

echo "Veces que aparece la vocal 'o':
"

grep -o -i "o" metamorphosis.txt > data4.txt

wc -l  data4.txt

echo "
"

echo "Veces que aparece la vocal 'u':
"

grep -o -i "u" metamorphosis.txt > data5.txt

wc -l  data5.txt

echo "
"

wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt

grep -o -i "a" Sainte-Beuve.txt > data6.txt

wc -l data6.txt > dataasainte.txt

paste dataasainte.txt dataametamorphosis.txt > dataComparacion.txt

echo "

El libro que más veces tiene la letra 'a' y cuántas veces aparece es:
"

awk dataComparacion.txt '{if($1 < $3) print "3864 del libro Sainte-Beuve"}'

awk dataComparacion.txt '{if($1 > $3) print "8080 del libro Metamorphosis"}'