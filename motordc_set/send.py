import serial
import time
 
serialArduino = serial.Serial('com6',9600)
def maju ():
    for i in range(20):
        serialArduino.write(b"M")
        serialArduino.write(b"+")
        time.sleep(0.5)
def kanan ():
    for i in range(20):
        serialArduino.write(b"R")
        serialArduino.write(b"+")
        time.sleep(0.5)
def kiri ():
    for i in range(20):
        serialArduino.write(b"L")
        serialArduino.write(b"+")
        time.sleep(0.5)
def stop():
     serialArduino.write(b"B")
     time.sleep(0.5)

while True:
    maju()
    #kanan()
    kanan()
    kiri()
    stop()
    #time.sleep(25)
    #stop()
    
   
    #serialArduino.write(b"L")
    #time.sleep(0.5)
 
