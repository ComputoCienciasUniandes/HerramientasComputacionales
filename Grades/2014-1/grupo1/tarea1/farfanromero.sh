wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt

echo "'nùmero de a's"

grep -o -i "a" metamorphosis.txt | wc -l > letras.txt

cat letras.txt


echo "'nùmero de e's"

grep -o -i "e" metamorphosis.txt   | wc -l




echo "'nùmero de i's"

grep -o -i "i" metamorphosis.txt | wc -l 




echo "'nùmero de o's"

grep -o -i "o" metamorphosis.txt | wc -l 




echo "'nùmero de u's"

grep -o -i "u" metamorphosis.txt  | wc -l
 

wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt


grep -o -i "a" Sainte-Beuve.txt | wc -l > aletras.txt





paste letras.txt aletras.txt > losdos.txt

awk'{if($1>$2)print "Metamorphosis tiene mas a" }' losdos.txt

echo "'nùmero de a's"

grep -o -i "a" metamorphosis.txt | wc -l 


