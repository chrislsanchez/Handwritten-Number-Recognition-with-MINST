"""
 code modified, tweaked and tailored from code by bertwert 
 on RPi forum thread topic 91796--plus raspi.tv
 csanchez
"""
import RPi.GPIO as GPIO
import sys
import os
import time
#import time
GPIO.setmode(GPIO.BCM)
 


Numerito = sys.argv[1]
 
# GPIO ports for the digit 0-3 pins 
digits = (23,22,27,17)
# 7seg_digit_pins (12,9,8,6) digits 0-3 respectively
 
for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)
 
num = {' ':(0,0,0,0),
    '0':(0,0,0,0),
    '1':(0,0,0,1),
    '2':(0,0,1,0),
    '3':(0,0,1,1),
    '4':(0,1,0,0),
    '5':(0,1,0,1),
    '6':(0,1,1,0),
    '7':(0,1,1,1),
    '8':(1,0,0,0),
    '9':(1,0,0,1)}
    
try:#exception handlers and/or cleanup code
#	GPIO.cleanup()
	for loop in range(0,3):
		GPIO.output(digits, num[Numerito])
		time.sleep(10)
            
except:
	print("some error")
	GPIO.cleanup()
            
finally:
	print("Terminating Display Number... Done!")
	GPIO.cleanup()
            
'''
try:#exception handlers and/or cleanup code
    while True:
        n = time.ctime()[11:13]+time.ctime()[14:16]
        s = str(n).rjust(4)
        for digit in range(4):
            for loop in range(0,7):
                GPIO.output(segments[loop], num[s[digit]][loop])
                if (int(time.ctime()[18:19])%2 == 0) and (digit == 1):
                    GPIO.output(25, 1)
                else:
                    GPIO.output(25, 0)
            GPIO.output(digits[digit], 0)
            time.sleep(0.001)
            GPIO.output(digits[digit], 1)
'''       
