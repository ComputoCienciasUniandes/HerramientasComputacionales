wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt

grep -o -i "a" metamorphosis.txt | wc -l
grep -o -i "e" metamorphosis.txt | wc -l
grep -o -i "i" metamorphosis.txt | wc -l
grep -o -i "o" metamorphosis.txt | wc -l
grep -o -i "u" metamorphosis.txt | wc -l

wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt

grep -o -i "a" Sainte-Beuve.txt | wc -l >>archivo2.txt
grep -o -i "a" metamorphosis.txt | wc -l >>archivo.txt

paste archivo.txt archivo2.txt > archivo3.txt

awk '{if($1>$2)print $1 "metamorphosis";else print $2 "Sainte-Beuve"}' archivo3.txt
