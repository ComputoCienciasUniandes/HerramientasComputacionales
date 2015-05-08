wget https://raw2.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt


grep -o -i "a" metamorphosis.txt | wc -l
grep -o -i "e" metamorphosis.txt | wc -l
grep -o -i "i" metamorphosis.txt | wc -l
grep -o -i "o" metamorphosis.txt | wc -l
grep -o -i "u" metamorphosis.txt | wc -l
grep -o -i "a" metamorphosis.txt | wc -l > file1a.dat

wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt

grep -o -i "a" sainte-beuve.txt | wc -l
grep -o -i "e" sainte-beuve.txt | wc -l
grep -o -i "i" sainte-beuve.txt | wc -l
grep -o -i "o" sainte-beuve.txt | wc -l
grep -o -i "u" sainte-beuve.txt | wc -l
grep -o -i "a" sainte-beuve.txt | wc -l > file2a.dat
 
echo -e file1a.dat \t file2a.dat > cantidades.dat

awk 'if{($1>$2) echo "Hay mas vocales a en metamorphosis.txt" else "Hay mas vocales a en Sainte-Beuve.txt"}' cantidades.dat
