wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt

echo 'a'
grep -o -i 'a' metamorphosis.txt | wc -l >> data1.txt
echo 'e'
grep -o -i 'e' metamorphosis.txt | wc -l
echo 'i'
grep -o -i 'i' metamorphosis.txt | wc -l
echo 'o'
grep -o -i 'o' metamorphosis.txt | wc -l
echo 'u'
grep -o -i 'u' metamorphosis.txt | wc -l


wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt

grep -o -i 'a' Sainte-Beuve.txt | wc -l >> data2.txt

paste data1.txt data2.txt >> data3.txt 

awk '{if($1>$2) print "El archivo Metamorfosis tiene más números de vocales que el archivo Sainte-Beuve con un total de:"}' data3.txt
awk '{if($1>$2) print $1}' data3.txt 

awk '{if($2>$1) print "El archivo Saitne-Beuve tiene más números de vocales que el archivo Sainte-Beuve Metamorfosis con un total de:"}' data3.txt
awk '{if($2>$1) print $2}' data3.txt 

rm *.txt

echo 'Gracias por utilizar el programa de conteo de Sergio Dìaz, Código 201224162'

