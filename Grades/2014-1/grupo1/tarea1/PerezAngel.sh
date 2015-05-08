wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt

echo "el numero de veces de a es"
grep -o -i "a" metamorphosis.txt |
wc -l  
echo "el numero de veces de e es"
grep -o -i "e" metamorphosis.txt|
 wc -l  
echo "el numero de veces de i es"
grep -o -i "i" metamorphosis.txt|
wc -l  
echo "el numero de veces de o es"
grep -o -i "o" metamorphosis.txt|
 wc -l  
echo "el numero de veces de u es"
grep -o -i "u" metamorphosis.txt|
 wc -l  

wget https://raw2.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt


grep -o -i "a" Sainte-Beuve.txt | wc -l > pepito.txt 

grep -o -i "a" metamorphosis.txt |wc -l  > meta.txt

paste pepito.txt meta.txt > vocales.txt

awk '{if($1<$2)print"metamorfosis tiene mas veces repetida la vocal a "}' vocales.txt
echo " y el numero de veces que aparece a es"
grep -o -i "a" metamorphosis.txt |wc -l 

awk '{if($1>$2)print"Sainte-Beuve  tiene mas veces repetida la vocal a"}' vocales.txt
 

rm metamorphosis.txt
rm pepito.txt 
rm meta.txt 
rm vocales.txt
rm Sainte-Beuve.txt