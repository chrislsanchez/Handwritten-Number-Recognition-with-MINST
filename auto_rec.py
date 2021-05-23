import RPi.GPIO as GPIO
import subprocess
import os
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(24, GPIO.FALLING)

#subprocess.call(['sudo', 'fswebcam', '-r', '28x28', '--no-banner', '~/TensorFlow/Rec_digitos/img/Foto.png'], shell=False)
#os.system("fswebcam -r 28x28 --no-banner /home/pi/TensorFlow/Rec_digitos/img/Foto.png")#make first time picture because of error: change cammera if possible!!
os.system("fswebcam -r 160x120 --no-banner /home/pi/TensorFlow/Rec_digitos/img/Foto.png")

os.system("python step_2_dig.py Foto True")
