wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt

echo "a"
 grep -o -i "a" metamorphosis.txt | wc -l
echo "e" 
grep -o -i "e" metamorphosis.txt | wc -l
echo "i"
grep -o -i "i" metamorphosis.txt | wc -l
echo "o"
grep -o -i "o" metamorphosis.txt | wc -l
echo "u"
grep -o -i "u" metamorphosis.txt | wc -l

wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt

echo "a"
grep -o -i "a" Sainte-Beuve.txt | wc -l

grep -o -i "a" metamorphosis.txt | wc -l > a1.txt
grep -o -i "a" Sainte-Beuve.txt | wc -l > a2.txt 

paste a1.txt a2.txt > aa.txt 

awk '{if ($1>$2) print "Metamorfosis tiene mas veces la vocal a,la tiene 8080 veces"}' aa.txt 

rm metamorphosis.txt
rm Sainte-Beuve.txt 






