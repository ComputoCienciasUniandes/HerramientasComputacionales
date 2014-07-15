wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/metamorphosis.txt
grep -i a  metamorphosis.txt | wc -l
grep -i e metamorphosis.txt | wc -l
grep -i i metamorphosis.txt | wc -l
grep -i o metamorphosis.txt | wc -l
grep -i u metamorphosis.txt | wc -l
wget https://raw.github.com/jngaravitoc/HerramientasComputacionales/master/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt
grep -i a Sainte-Beuve.txt | wc -l
paste metamorphosis.txt Saint-Beuve.txt > MolanoParrado.txt
paste metamorphosis.txt Sainte-Beuve.txt > MolanoParrado.txt
