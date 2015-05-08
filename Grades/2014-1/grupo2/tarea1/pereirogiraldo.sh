wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt
grep -o -i a metamorphosis.txt | wc -l
grep -o -i e metamorphosis.txt | wc -l
grep -o -i i metamorphosis.txt | wc -l
grep -o -i o metamorphosis.txt | wc -l
grep -o -i u metamorphosis.txt | wc -l

wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt
grep -o -i a metamorphosis.txt | wc -l >> kafkametamorphosis.txt
grep -o -i a Sainte-Beuve.txt | wc -l >> fernandsainte.txt

paste kafkametamorphosis.txt fernandsainte.txt > total.txt

awk '{if($1<$2) print "Hay mayor cantidad de a en Sainte Beuve con "$2 }' total.txt
awk '{if($2<$1) print "Hay mayor cantidad de a en Metamorphosis con " $1 }' total.txt
