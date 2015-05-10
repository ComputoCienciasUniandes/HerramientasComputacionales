wget https://raw2.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt


grep -o -i "a" metamorphosis.txt | wc -l > a.txt
cat a.txt
grep -o -i "e" metamorphosis.txt | wc -l > e.txt
cat e.txt
grep -o -i "i" metamorphosis.txt | wc -l > i.txt
cat i.txt
grep -o -i "o" metamorphosis.txt | wc -l > o.txt
cat o.txt
grep -o -i "u" metamorphosis.txt | wc -l > u.txt
cat u.txt

wget https://raw2.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt

grep -o -i "a" Sainte-Beuve.txt | wc -l > a1.txt


paste a.txt a1.txt | wc -l > A.txt

awk '{if ($1 > $2) print "La Metamorfosis tiene más aes" }' A.txt
awk '{if ($1 < $2) print "Saint Beuve tiene más aes " }' A.txt


