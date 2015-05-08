wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt
grep -o -i a metamorphosis.txt | wc -l
grep -o -i e metamorphosis.txt | wc -l
grep -o -i i metamorphosis.txt | wc -l
grep -o -i o metamorphosis.txt | wc -l
grep -o -i u metamorphosis.txt | wc -l

wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt

grep -o -i a metamorphosis.txt | wc -l >> cuentametamorphosis.txt
grep -o -i a Sainte-Beuve.txt | wc -l >> cuentasaintebeuve.txt

paste cuentametamorphosis.txt cuentasaintebeuve.txt > cuentatotal.txt

awk ' {if($1<$2) print "Hay mas veces a en Sainte Beuve con "$2 }' cuentatotal.txt
awk  ' {if($2<$1) print "Hay mas veces a en Metamorphosis con "$1 }' cuentatotal.txt
