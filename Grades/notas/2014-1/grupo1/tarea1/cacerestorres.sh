wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt


echo "a Metamorphosis"
grep -i -o "a" metamorphosis.txt | wc -l  
echo "e"
grep -i -o "e" metamorphosis.txt | wc -l
echo "i"
grep -i -o "i" metamorphosis.txt | wc -l
echo "o" 
grep -i -o "o" metamorphosis.txt | wc -l
echo "u"
grep -i -o "u" metamorphosis.txt | wc -l


echo "a Sainte-Beuve"
grep -i -o "a" Sainte-Beuve.txt | wc -l


grep -o "a" metamorphosis.txt | wc -l > V1.txt
grep -o " a" Sainte-Beuve.txt | wc -l > V2.txt
paste V1.txt V2.txt > Abook.txt
awk '{if ($1 > $2) print "Metamorphosis tiene mayor numero de vocales  A"}' Abook.txt


 





