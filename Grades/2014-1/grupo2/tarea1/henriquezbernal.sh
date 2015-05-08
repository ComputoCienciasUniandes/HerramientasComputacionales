wget  https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt

echo "a :"
 grep -o -i 'e' metamorphosis.txt | wc -l
 grep -o -i 'a' metamorphosis.txt | wc -l > Ametamorfosis.txt
echo "e :"
 grep -o -i 'e' metamorphosis.txt | wc -l
 grep -o -i 'e' metamorphosis.txt | wc -l > Emetamorfosis.txt
echo "i :"
 grep -o -i 'i' metamorphosis.txt | wc -l
 grep -o -i 'i' metamorphosis.txt | wc -l > Imetamorfosis.txt
echo "o :"
 grep -o -i 'o' metamorphosis.txt | wc -l
 grep -o -i 'o' metamorphosis.txt | wc -l > Ometamorfosis.txt
echo "u :"
 grep -o -i 'u' metamorphosis.txt | wc -l
 grep -o -i 'u' metamorphosis.txt | wc -l > Umetamorfosis.txt

wget https://github.com/jngaravitoc/HerramientasComputacionales/blob/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt
 
echo "as :"
 grep -o -i 'a' Sainte-Beuve.txt | wc -l &
 grep -o -i 'a' Sainte-Beuve.txt | wc -l > ASainte-Beuv.txt
echo "e :"
 grep -o -i 'a' Sainte-Beuve.txt | wc -l &
 grep -o -i 'e' Sainte-Beuve.txt | wc -l > ESainte-Beuv.txt 
echo "i :"
 grep -o -i 'i' Sainte-Beuve.txt | wc -l &
 grep -o -i 'i' Sainte-Beuve.txt | wc -l > ISainte-Beuv.txt
echo "o :"
 grep -o -i 'o' Sainte-Beuve.txt | wc -l &
 grep -o -i 'o 'Sainte-Beuve.txt | wc -l > OSainte-Beuv.txt
echo "u :"
 grep -o -i 'u' Sainte-Beuve.txt | wc -l &
 grep -o -i 'u' Sainte-Beuve.txt | wc -l > USainte-Beuv.txt

paste Ametamorfosis.tx ASainte-Beuv.txt > data.txt

awk '{if($1>$2)print $0}'data.txt
cat data.txt
awk '{if($2>$1)print $0}'data.txt
cat data.txt
&

