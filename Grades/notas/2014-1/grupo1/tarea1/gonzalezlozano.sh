wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt

wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt

echo "a metamorphosis"
grep -i -o "a" metamorphosis.txt |wc -l
echo "e metamorphosis"
grep -i -o "e" metamorphosis.txt |wc -l
echo "i metamorphosis"
grep -i -o "i" metamorphosis.txt |wc -l
echo "o metamorphosis"
grep -i -o "o" metamorphosis.txt |wc -l
echo "u metamorphosis"
grep -i -o "u" metamorphosis.txt |wc -l

echo "a Sainte-Beuve"
grep -i -o "a" Sainte-Beuve.txt |wc -l
echo "e Sainte-Beuve"
grep -i -o "e" Sainte-Beuve.txt |wc -l
echo "i Sainte-Beuve"
grep -i -o "i" Sainte-Beuve.txt |wc -l
echo "o Sainte-Beuve"
grep -i -o "o" Sainte-Beuve.txt |wc -l
echo "u Sainte-Beuve"
grep -i -o "u" Sainte-Beuve.txt |wc -l

grep -i -o "a" metamorphosis.txt |wc -l > ametamorphosis.txt
grep -i -o "a" Sainte-Beuve.txt |wc -l > asaintebeuve.txt

paste ametamorphosis.txt asaintebeuve.txt > nombre.txt
awk '{if($1 > $2) print "Metamorfosis tiene mas a"}' nombre.txt
 

