wget https://raw2.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt
wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt

grep -o -i 'a' metamorphosis.txt | wc -l > a.dat
grep -o -i 'e' metamorphosis.txt | wc -l > e.dat
grep -o -i 'i' metamorphosis.txt | wc -l > i.dat
grep -o -i 'o' metamorphosis.txt | wc -l > o.dat
grep -o -i 'u' metamorphosis.txt | wc -l > u.dat

echo 'La vocal "a" aparece'
cat a.dat
echo 'veces'

echo 'La vocal "e" aparece'
cat e.dat
echo 'veces'

echo 'La vocal "i" aparece'
cat i.dat
echo 'veces'

echo 'La vocal "o" aparece'
cat o.dat
echo 'veces'

echo 'La vocal "u" aparece'
cat u.dat
echo 'veces'

rm a.dat
rm e.dat
rm i.dat
rm o.dat
rm u.dat

 
grep -o -i 'a' metamorphosis.txt | wc -l > meta.dat
grep -o -i 'a' Sainte-Beuve.txt | wc -l > sainte.dat

paste meta.dat sainte.dat > data.dat

awk '{if($1>2)print "a aparece mas en meta con = "$1" veces"}' data.dat


rm meta.dat
rm sainte.dat
rm data.dat
rm metamorphosis.txt
rm Sainte-Beuve.txt
