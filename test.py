import RPi.GPIO as GPIO
from time import sleep

"""Configura los leds en modo salida"""
#voltaje
COL1 = 15
COL2 = 18
ROW1 = 19
ROW2 = 26
cols = [COL1, COL2]
rows = [ROW1, ROW2]
def setup_leds():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(cols, GPIO.OUT)
    #tierra
    GPIO.setup(rows, GPIO.OUT)

def leds_off():
    """Apaga todos los leds al enviar el mismo voltaje al catodo y anodo del diodo"""
    GPIO.output(cols, GPIO.HIGH)
    GPIO.output(rows, GPIO.HIGH)

setup_leds()
try:
    while 1:
        leds_off()
        #GPIO.output(COL1, GPIO.HIGH)
        GPIO.output(ROW1, GPIO.LOW)
        sleep(0.1)
        leds_off()
        #GPIO.output(COL1, GPIO.HIGH)
        GPIO.output(ROW2, GPIO.LOW)
        sleep(0.1)
        leds_off()
except KeyboardInterrupt:
    GPIO.cleanup()