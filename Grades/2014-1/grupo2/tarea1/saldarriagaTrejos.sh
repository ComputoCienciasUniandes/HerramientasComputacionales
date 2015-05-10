#!/bin/sh
echo "Hola, esta es la primera tarea de herramientas computacionales"

emacs Datos1.txt &
wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt


grep a metamorphosis.txt| wc>>Datos1.txt
grep e metamorphosis.txt| wc>>Datos1.txt
grep i metamorphosis.txt| wc>>Datos1.txt
grep o metamorphosis.txt| wc>>Datos1.txt
grep u metamorphosis.txt| wc>>Datos1.txt

emacs Datos2.txt &
wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt

grep a Sainte-Beuve.txt| wc>>Datos2.txt
grep e Sainte-Beuve.txt| wc>>Datos2.txt
grep i Sainte-Beuve.txt| wc>>Datos2.txt
grep o Sainte-Beuve.txt| wc>>Datos2.txt
grep u Sainte-Beuve.txt| wc>>Datos2.txt

emacs comparacion.txt
paste Datos1.txt Datos2.txt>comparacion.txt

echo "El texto que tiene el mayor numero de letras a es: metamorphosis.txt la cual parece 2667 veces"