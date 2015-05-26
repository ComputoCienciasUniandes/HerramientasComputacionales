#!/bin/bash
shopt -s expand_aliases
alias myfig="figlet -c -w $(tput cols)"
alias hal="read -n 1 -s"
alias centerfig="figlet -c -w $(tput cols) -f term"

if [ -t 0 ]; then stty -echo -icanon time 0 min 0; fi

roo="./"
count=0
keypress=''
while [ "x$keypress" = "x" ]; do
  let count+=1
  printf $(head -$count hygxyz.csv | tail -1)
  sleep $(($RANDOM % 2))
  read keypress
done

if [ -t 0 ]; then stty sane; fi
echo ""
read -n 1 -s
clear
cat ./Art/andes | figlet -c -w $(tput cols) -f term
myfig "||   uniandes   ||"
read -n 1 -s
clear
myfig "Herramientas"
myfig "Computacionales"
read -n 1 -s
cat ./Art/terminal_welcome | figlet -c -w $(tput cols) -f term
myfig "Juan David Lizarazo"
# read -n 1 -s
# myfig "jd.lizarazo10@unia..."
read -n 1 -s
clear
myfig "Programa"
hal
clear
myfig "||  Semana 1  ||"
myfig "Consola."
myfig "Comandos basicos de"
cat ./Art/unix | figlet -c -w $(tput cols) -f term
printf "\n\n"
echo "-- ls -- cd -- kill -- mkdir -- tar -- cp -- rm -- mv -- chmod -- grep -- awk -- ps -- sudo -- ssh -- sftp -- gzip -- history -- man -- date -- top --" | figlet -c -w $(tput cols) -f term
hal
clear
myfig "||  Semana 2  ||"
myfig "Editores de texto"
myfig "Vi"
hal
vi ~/.bash_profile
# myfig "||  Semana 2  ||"
# myfig "Editores de texto"
# myfig "Emacs"
# hal
clear
myfig "||  Semanas 3-4  ||"
myfig "LaTeX"
cat ./Art/eqn1 | figlet -c -w $(tput cols) -f term
hal
vi ~/Dropbox/UAndes/Herramientas-Computacionales-Private/duperTangle.tex
open ~/Dropbox/UAndes/Herramientas-Computacionales-Private/duperTangle.pdf
hal
clear
myfig "||  Semana 5-8  ||"
myfig "Python"
printf "\n"
cat ./Art/pythonlogo | figlet -c -w $(tput cols) -f term
hal
clear
myfig "||  Semanas 9-14  ||"
myfig "Metodos Numericos"
hal
myfig "Analisis de datos"
hal
myfig "NumPy"
hal
myfig "Estadistica"
hal
myfig "Monte Carlo"
hal
myfig "Algebra lineal"
hal
clear
myfig "Forma de Evaluacion"
centerfig "Talleres (70%), eliminando la mejor y la peor nota."
centerfig "Examenes cortos (30%)"
hal
