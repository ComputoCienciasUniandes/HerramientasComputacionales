wget https://raw2.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt
wget https://raw2.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt
grep -i -o a metamorphosis.txt|wc|awk '{ print  "a" , $1 }'
grep -i -o e metamorphosis.txt|wc|awk '{ print  "e" , $1 }'
grep -i -o i metamorphosis.txt|wc|awk '{ print  "i" , $1 }'
grep -i -o o metamorphosis.txt|wc|awk '{ print  "o" , $1 }'
grep -i -o u metamorphosis.txt|wc|awk '{ print  "u" , $1 }'
grep -i -o a metamorphosis.txt|wc>data1.dat
grep -i -o a Sainte-Beuve.txt|wc|>data2.dat
paste data1.dat data2.dat>data.dat
awk '{ if($1>$4)print "Metamorfosis", $1 }' data.dat
awk '{ if($1<$4)print "Sainte-Beuve", $4 }' data.dat
awk '{ if($1==$4)print "Iguales", $1 }' data.dat
