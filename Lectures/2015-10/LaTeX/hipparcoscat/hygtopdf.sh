#!/bin/bash
# ------------------------------------------------------------------
# Title			hygtopdf		
# Description	Takes the catalog, constructs a valid LaTeX file for it and compiles it.		
# Author		Juan David Lizarazo
# Creation Date	Feb 9, 2015
# ------------------------------------------------------------------

#First make sorted catalogue
if [ ! -f ./sortedhyg.csv ]; then
	echo "Sorted catalogue not found, will create now."
	head -1 hyg.csv > header
	grep -v "Proper Name" hyg.csv > sortedhyg.csv
	sort --field-separator="," --key=10 -n sortedhyg.csv > sortedhyg2.csv
	cat header sortedhyg2.csv > sortedhyg.csv
	rm sortedhyg2.csv
	rm header
fi
#Now construct the header of the tex file
echo "\documentclass{article}
\usepackage{longtable}
\usepackage[letterpaper,margin=1in,landscape]{geometry}
\usepackage{graphicx}
\usepackage{fancyhdr}
\usepackage{amsfonts}
\pagestyle{fancy}
%\pagestyle{empty}
%\pagenumbering{gobble}
\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\footrulewidth}{0.6pt}
\fancyfoot[C]{\textsc{Page }\thepage}
\chead{$\star \star \star \star \star$ \textsc{hyg Catalog of Stars} $\star \star \star \star \star$}
\begin{document}
\thispagestyle{empty}
\small
\begin{center}
	\includegraphics[width=0.5\textwidth]{title.png}
\end{center}
\begin{longtable}{|c|c|c|c|c|c|c|c|c|}
\hline
" > hygcat.tex
#First put the named stars
awk -F"," '{if(($7!="")&&($2!="0")) print $2","$7","$8","$9","$10","$14","$15","$16","$17}' sortedhyg.csv | sed 's/$/ \\\\ \\hline /g' | sed 's/\,/ \& /g' >> hygcat.tex
#Next put the anonymous stars
cat sortedhyg.csv | awk -F"," '{if(($7=="")&&($2!="0")) print $2","$7","$8","$9","$10","$14","$15","$16","$17}' | sed 's/$/ \\\\ \\hline /g' | sed 's/\,/ \& /g' >> hygcat.tex
#Now finish the tex file
echo "\end{longtable}" >> hygcat.tex
echo "\end{document}" >> hygcat.tex
#Make the fist line the header
sed '/^HIP/ s/\\\\/\\\\ \\hline \\hline \\endhead /' hygcat.tex > hygcat2.tex
mv hygcat2.tex hygcat.tex
#Compile tex
pdflatex hygcat.tex
#Must compile again for the height of the tables to come out right
pdflatex hygcat.tex
#Open the file
open hygcat.pdf
