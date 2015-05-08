wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt

    echo 'El número de letras A es'
 grep "a" -i -o metamorphosis.txt| wc -l
    echo 'El número de letras E es'
 grep "e" -i -o metamorphosis.txt|  wc -l
    echo 'El número de letras I es' 
grep "i" -i -o metamorphosis.txt| wc -l
    echo 'El número de letras O es' 
grep "o" -i -o metamorphosis.txt| wc -l
    echo 'El número de letras U es' 
grep "u" -i -o metamorphosis.txt| wc -l

wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt

grep "a" -i -o metamorphosis.txt| wc -l >> dataMeta.txt
grep "a" -i -o Sainte-Beuve.txt| wc -l >> dataSainte.txt
paste dataMeta.txt dataSainte.txt > dataMetaSainte.txt

awk '{if($1>$2) print "El archivo que contiene más veces la letra A es metamorphosis con un número de " $1 }' dataMetaSainte.txt 

awk '{if($1<$2) print "El archivo que contiene más veces la letra A es Saint-Beuve con un número de" $2 }' dataMetaSainte.txt 

echo "Por Juan Sebastian Garzón Alvarado-201212076"
