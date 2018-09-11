try:
    import RPi.GPIO as GPIO
except (RuntimeError, ModuleNotFoundError):
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.")
from time import sleep
import threading

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

def nose():
    try:
        while 1:
            print("Esto es una secuencia")
            sleep(5)
    except KeyboardInterrupt:
        print("Detenido")
threading.Thread(target=nose).start()