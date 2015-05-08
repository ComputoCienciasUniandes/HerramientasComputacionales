wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt

echo " Numero de vocales de todo Metamorphosis es:"
echo "a:"
grep -c -i a metamorphosis.txt
echo "e:"
grep -c -i e metamorphosis.txt
echo "i:"
grep -c -i i metamorphosis.txt
echo "o:"
grep -c -i o metamorphosis.txt
echo "u:"
grep -c -i u metamorphosis.txt



wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt

echo "Metamorphosis tiene mas vocales 'a' con"
grep -c -i a metamorphosis.txt