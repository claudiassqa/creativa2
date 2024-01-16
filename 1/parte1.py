#!/usr/bin/python3
import os, sys, subprocess
from subprocess import call

#Instalar desde github, instalar Python3 y pip y cambio a la carpeta en la que quiero trabajar
call(["sudo apt-get -y install git"], shell=True)
call(["sudo apt-get -y update "], shell=True)
call(["sudo apt-get -y install python3-pip "], shell=True)
call(["git clone https://github.com/CDPS-ETSIT/practica_creativa2.git"], shell=True)
os.chdir('practica_creativa2/bookinfo/src/productpage')

#Instalar lista de dependencias 
call(["sudo pip3 install -r requirements.txt"], shell=True)

#Asignación de la variable global
os.environ["GRUPO_NUMERO"] = "23"

#Modificamos el titulo del html
fin=open("templates/productpage.html", "r")
fout=open("templates/grupo.html", "w")

for line in fin:
    if "Simple Bookstore App" in line:
            fout.write('''{% block title %}'''+ os.environ['GRUPO_NUMERO'] + '''{% endblock %}''')
    else:
            fout.write(line)
fin.close()
fout.close()

call(["mv templates/grupo.html templates/productpage.html"], shell=True)
call(["rm grupo.html"], shell=True)

#Habilitamos el puerto 9080 y lanzamos aplicación
os.system("python3 productpage_monolith.py 9080")