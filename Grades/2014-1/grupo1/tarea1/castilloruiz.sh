wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt

echo " La a se repite "
grep -o -i "a" metamorphosis.txt | wc -l > vocala.txt

cat vocala.txt

echo " La e se repite "

grep -o -i "e" metamorphosis.txt | wc -l > vocale.txt

cat vocale.txt

echo " La i se repite "

grep -o -i "i" metamorphosis.txt | wc -l > vocali.txt 

cat vocali.txt

echo " La o se repite "

grep -o -i "o" metamorphosis.txt | wc -l > vocalo.txt

cat vocalo.txt

echo "La u se repite "

grep -o -i "u" metamorphosis.txt | wc -l > vocalu.txt

cat vocalu.txt

wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt

grep -o -i "a" Sainte-Beuve.txt | wc -l > vocala2.txt


paste vocala.txt vocala2.txt | wc -l > comparacion.txt

echo "El libro que tiene mayor  numero de a es:"

awk '{ if ($1 > $2) print " La metamrfosis" }' comparacion.txt

awk '{ if ($1 < $2) print " Saint-Beuve " }' comparacion.txt










