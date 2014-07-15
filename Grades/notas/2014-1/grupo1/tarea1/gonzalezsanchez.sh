wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt 
echo El numero de veces que a aparece 
grep -i -c 'a' metamorphosis.txt; 
echo El numero de veces que e aparece ;
grep -i -c 'e' metamorphosis.txt ;
echo El numero de veces que i aparece ;
grep -i -c 'i' metamorphosis.txt;
echo El numeo de veces que o aparece ;
grep -i -c 'o' metamorphosis.txt ;
echo El numero de veces que u aparece ;
grep -i -c 'u' metamorphosis.txt;

wget https://github.com/jngaravitoc/HerramientasComputacionales/blob/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt

if [$"grep -i -c 'a' metamorphosis.txt" -lt $"grep -i -c 'a' Sainte-Beuve.txt"];
then 
 echo "Hay mas letras a en Sainte-Beuve"
else 
 echo "Hay mas letras a en Metamorphosis"
fi