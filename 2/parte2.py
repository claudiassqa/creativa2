import os, sys, subprocess
from subprocess import call

call(["sudo apt-get -y update "], shell=True)
call(["sudo apt -y install docker.io "], shell=True)

call ("sudo docker build -t g23/product-page .", shell=True)
call ("docker run  --name g23-product-page -p 9080:9080 -e GRUPO_NUMERO=23 -d g23/product-page", shell=True)




