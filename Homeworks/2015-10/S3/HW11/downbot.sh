#!/bin/bash
pad="0"
for i in {1..22}
do
if [ $i -eq 10 ]
then
	pad=""
fi
thefilename=hs_alt_CHM1_1.1_chr$i.fa.gz
theurl=ftp://ftp.ncbi.nih.gov/genomes/Homo_sapiens/CHR_$pad$i/
wget $theurl$thefilename
gunzip -c $thefilename > cromo$i.fa
done