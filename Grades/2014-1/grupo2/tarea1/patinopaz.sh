wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt 
echo "A's Metamorphosis" 
grep -i -o "a" metamorphosis.txt | wc -l 
echo "E's Metamorphosis" 
grep -i -o "e"  metamorphosis.txt | wc -l 
echo "I's Metamorphosis" 
grep -i -o "i" metamorphosis.txt  | wc -l 
echo "O's Metamorphosis" 
grep -i -o "o" metamorphosis.txt | wc -l 
echo "U's Metamorphosis" 
grep -i -o "u" metamorphosis.txt | wc -l 

wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt

grep -i -o "a" metamorphosis.txt | wc -l > ametamorphosis.txt
grep -i -o "a" Sainte-Beuve.txt | wc -l > asaintbeuve.txt 

paste ametamorphosis.txt asaintbeuve.txt > nombre.txt
awk '{if($1 > $2) print "Metamorfosis tiene más a"}' nombre.txt

 

