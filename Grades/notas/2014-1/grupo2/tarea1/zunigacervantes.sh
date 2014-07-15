echo " Nùmero de vocales de todo Metamorphosis"
echo "a:"
grep -i -o  a metamorphosis.txt.3| wc -l
echo "e:"
grep -i -o  e metamorphosis.txt.3| wc -l
echo "i"
grep -i -o  i metamorphosis.txt.3| wc -l
echo "o"
grep -i -o  o metamorphosis.txt.3| wc -l
echo "u"
grep -i -o  u metamorphosis.txt.3| wc -l

awk '{if($1 > $2) print "Metamorphosis tiene mas a"}' javierzuniga.txt
echo "con:"
grep -i -o  a metamorphosis.txt.3| wc -l