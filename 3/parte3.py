import os, sys, subprocess
from subprocess import call

call(["sudo apt-get -y update "], shell=True)
call(["sudo apt-get -y upgrade "], shell=True)
call(["sudo apt-get -y install git "], shell=True)
call(["sudo apt-get -y install python3-pip "], shell=True)
call(["sudo apt -y install docker.io "], shell=True)
call(["sudo apt -y install docker-compose  "], shell=True)

call(["git clone https://github.com/CDPS-ETSIT/practica_creativa2.git"], shell=True)


call ("docker build -t g23/product-page -f ./product-page/Dockerfile .", shell=True)
call ("docker build -t g23/details -f ./details/Dockerfile .", shell=True)
call ("docker build -t g23/ratings -f ./ratings/Dockerfile .", shell=True)

call ('docker run --rm -u root -v "$(pwd)/practica_creativa2/bookinfo/src/reviews":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build' , shell=True)

call ("docker build -t g23/reviews-v1 -f ./reviews/Dockerfile --build-arg service_version=v1 --build-arg enable_ratings=false --build-arg star_color='black' .", shell=True)
call ("docker build -t g23/reviews-v2 -f ./reviews/Dockerfile --build-arg service_version=v2 --build-arg enable_ratings=true --build-arg star_color='black' .", shell=True)
call ("docker build -t g23/reviews-v3 -f ./reviews/Dockerfile --build-arg service_version=v3 --build-arg enable_ratings=true --build-arg star_color='red' .", shell=True)

call("docker-compose up", shell=True)
