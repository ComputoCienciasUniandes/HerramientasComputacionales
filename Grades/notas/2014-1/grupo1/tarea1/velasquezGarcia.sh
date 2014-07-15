wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt
grep -o -i "a" metamorphosis.txt | wc -l > letrasA.txt 
grep -o -i "e" metamorphosis.txt | wc -l > letrasE.txt 
grep -o -i "i" metamorphosis.txt | wc -l > letrasI.txt 
grep -o -i "o" metamorphosis.txt | wc -l > letrasO.txt 
grep -o -i "u" metamorphosis.txt | wc -l > letrasU.txt 
cat letrasA.txt 
cat letrasE.txt 
cat letrasI.txt 
cat letrasO.txt 
cat letrasU.txt 
wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt
grep -o -i "a" Sainte-Beuve.txt | wc -l > letrasA2.txt
grep -o -i "e" Sainte-Beuve.txt | wc -l > letrasE2.txt
grep -o -i "o" Sainte-Beuve.txt | wc -l > letrasO2.txt
grep -o -i "i" Sainte-Beuve.txt | wc -l > letrasI2.txt
grep -o -i "u" Sainte-Beuve.txt | wc -l > letrasU2.txt
cat letrasA2.txt
cat letrasE2.txt
cat letrasI2.txt
cat letrasO2.txt
cat letrasU2.txt
awk  {'if ( letrasA -gt letrasA2 ) print "Metamorphosys tiene mas letras a: 8080"'} letrasA.txt &
awk  {'if ( letrasA2 -gt  letrasA ) print "Sainte-Beuve tiene mas letras a: 3864"'} &

