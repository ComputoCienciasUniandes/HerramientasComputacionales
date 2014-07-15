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

grep -o -i "a" metamorphosis.txt | wc -l > cualtienemasa.txt
grep -o -i "a" Sainte-Beuve.txt | wc -l > cualtienemasa2.txt

paste cualtienemasa.txt cualtienemasa2.txt > atotal.txt

awk '{if($1>$2)print "el libro de metamorfósis tiene más volcales a y aparece repetida 8080 veces"}' atotal.txt

rm metamorphosis.txt
rm Sainte-Beuve.txt



