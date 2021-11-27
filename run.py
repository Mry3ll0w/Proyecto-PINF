import os
import sys
import platform

#Este script vale para evitar tener que hacer python manage ...
#y automatizar el proceso de forma mas sencilla

#Con sys obtendremos un argumento para asi seleccionar como y cuando runear el server
#1) el argumento es localhost ==> se runea con el local
#2) el argumento es server ==> se runea con el server de digital ocean en una ip y puerto concretos

#Gracias a la libreria platform obtendremos en que sistema estamos para runear el servidor de forma correcta

if platform.system() == 'Windows':

    if sys.argv[1] == 'local':
        os.system("python3 prpinf/manage.py runserver")
    elif sys.argv[1] == 'server':
        os.system("python3 prpinf/manage.py runserver 161.35.37.208:8000")

elif platform.system() == 'Linux':

    if sys.argv[1] == 'local':
        os.system("python3 prpinf/manage.py runserver")
    elif sys.argv[1] == 'server':
        os.system("python3 prpinf/manage.py runserver 161.35.37.208:8000")

else:
    print("Argumentos incorrectos\nEstos deben seguir la forma:\n")
    print("python run.py [local/server]")
    print("EJ:\nQuiero abrir el servidor en local==> python run.py local")
