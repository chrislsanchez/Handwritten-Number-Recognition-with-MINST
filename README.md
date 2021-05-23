# Playground_ML_Rpi

This file contains the folder TensorFlow with the MNIST

OS: Raspbian 8.0 Jessie : 02/03/2017
Tensorflow V1.1

Inside you will find the following scripts:

1. /tensorflow-minst
clonned repo from
https://github.com/opensourcesblog/tensorflow-mnist.git
Original Post:
https://medium.com/@o.kroeger/tensorflow-mnist-and-your-own-handwritten-digits-4d1cd32bbab4

2. /Rec_digitos
based in the above repo, this folder uses a push button (Normal Open) to take a foto using a web cammera and displaying the prediction using a BCD format

GPIO 24 -> push button

BCD
GPIO23	--MSB
GPIO22
GPIO27
GPIO17	--LSB


SCRIPTS:
----------------------------
mnist.py:
----------------------------
normal trains and make prediction of images using the MNIST data base
-----------------------------


----------------------------
step_2.py
----------------------------
Original from repo. Can predict with your own images. copy and paste the Imagen.png in folder img and use in the console

$ python step_2_dig.py Imagen True

use True if the number is black with withe background. Number white with black background uses False
----------------------------

----------------------------
digitos.py
----------------------------
This script displays a given number in BCD code in the above mentioned ports during 10 seconds

to display number 5:

$ sudo python digitos.py 5

----------------------------
step_2_dig.py
----------------------------
Modified script from original, makes the prediction and displays the value usong digitos.py

$ python step_2_dig.py Foto True

----------------------------
auto_rec.py
----------------------------
Automatically makes a picture using a web cammera and stores the taken picture in folder /img with the name Foto.png

runs the step_2_dig with the taken foto making the prediction and displaying it in BCD format

after executing, it waits for the pulser to be pressed.

$ sudo auto_rec.py 