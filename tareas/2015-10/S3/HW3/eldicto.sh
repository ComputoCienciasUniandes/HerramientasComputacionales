#!/bin/bash
# Tercer taller del curso Herramientas Computacionales
# Universidad de los Andes
# Autor: Juan David Lizarazo
# Fecha: 18-Feb-2015
# El encabezado del documento en LaTeX
echo "\documentclass[8pt,twocolumn]{article}" > eldicto.tex
echo "\usepackage{fontspec,xltxtra,xunicode}" >> eldicto.tex
echo "\usepackage{graphicx}" >>  eldicto.tex
echo "\usepackage{color}" >>  eldicto.tex
echo "\setmainfont{Times New Roman}" >> eldicto.tex
echo '\begin{document}' >>  eldicto.tex
echo '\begin{center}' >>  eldicto.tex
echo '\includegraphics[width=7.5cm]{./lainicial.png}' >>  eldicto.tex
echo '\end{center}' >>  eldicto.tex
echo '\begin{description}' >> eldicto.tex
# En este punto, usando sed, se modifican los datos para obedecer el formato LaTeX
sed 's/^/\\item\[/g' laletraa.txt | sed 's/;;/]/g' | sed -E 's/ (m|f|adj|tr|adj|adv|intr|loc|prnl|desus|com|coloq|ant)\./\\textit{ \1.}/g' | sed -E 's/([0-9]?[0-9])\./ {\\color{blue} \1.} /g'  >> eldicto.tex
# Terminar lo necesario para tener un archivo de LaTeX compilable.
echo '\end{description}' >> eldicto.tex
echo '\end{document}' >> eldicto.tex
# Compilar
xelatex eldicto.tex
# Abrir el pdf, específico para Mac
open eldicto.pdf &
