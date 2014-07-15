wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt
echo "El nùmero de veces que aparece la letra "a" es"
grep -o -i "a" metamorphosis.txt | wc -l > letraa.txt
cat letraa.txt

echo "El nùmero de veces que aparece la letra "e" es"
grep -o -i "e" metamorphosis.txt | wc -l > letrae.txt
cat letrae.txt

echo "El nùmero de veces que aparece la letra "i" es"
grep -o -i "i" metamorphosis.txt | wc -l > letrai.txt
cat letrai.txt

echo "El nùmero de veces que aparece la letra "o" es"
grep -o -i "o" metamorphosis.txt | wc -l > letrao.txt
cat letrao.txt

echo "El nùmero de veces que aparece la letra "u" es"
grep -o -i "u" metamorphosis.txt | wc -l > letrau.txt
cat letrau.txt

wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt
grep -o -i "a" Sainte-Beuve.txt | wc -l >letraaa.txt
echo "el libro que tiene màs veces la vocal "a" repetida es:"
paste letraa.txt letraaa.txt >a.txt
awk '{if($1>$2)print"La Metamorfosis, donde aparece el siguiente nùmero de veces:"}' a.txt
cat letraa.txt

   


 