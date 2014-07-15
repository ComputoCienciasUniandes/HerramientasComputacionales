rm *.txt
wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt
grep -o -i a metamorphosis.txt | wc -w >> meta.txt
cat meta.txt
grep -o -i e metamorphosis.txt | wc -w
grep -o -i i metamorphosis.txt | wc -w
grep -o -i o metamorphosis.txt | wc -w
grep -o -i u metamorphosis.txt | wc -w

wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt
grep -o -i a Sainte-Beuve.txt | wc -w >> sainte.txt
cat sainte.txt

paste meta.txt sainte.txt > data.txt
awk '{s += $1; p += $2; u = "Sainte-Beuve "; v = p; if(s > p){ v = s; u = "La metamorphosis "}} END {print u "tiene " v " letras 'a'" }' data.txt

