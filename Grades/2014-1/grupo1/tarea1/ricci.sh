wget https://raw2.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt

grep -o -i "a" metamorphosis.txt | wc -l > letraa.txt
cat letraa.txt

grep -o -i "e" metamorphosis.txt | wc -l > letrae.txt
cat letrae.txt

grep -o -i "i" metamorphosis.txt | wc -l > letrai.txt
cat letrai.txt

grep -o -i "o" metamorphosis.txt | wc -l > letrao.txt
cat letrao.txt

grep -o -i "u" metamorphosis.txt | wc -l > letrau.txt
cat letrau.txt

wget https://raw2.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt

grep -o -i "a" Sainte-Beuve.txt | wc -l > letraas.txt

paste letraa.txt letraas.txt > holas.txt


awk '{if($1 > $2) print "El libro Metamorfosis tiene más letras A que Sainte-Beuve y aparece " $1 " veces"}' holas.txt

awk '{if($1 < $2) print "El libro Sainte-Beuve tiene más letras A que Metamorfosis e y aparece " $2 " veces"}' holas.txt



