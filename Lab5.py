import RPi.GPIO as GPIO
from time import sleep

# Columnas
COL1 = 26
COL2 = 19
COL3 = 13
COL4 = 6
COL5 = 5

# Filas
ROW1 = 21
ROW2 = 20
ROW3 = 16
ROW4 = 12
ROW5 = 1
ROW6 = 7
ROW7 = 8
columns = [COL1, COL2, COL3, COL4, COL5]
rows = [ROW1, ROW2, ROW3, ROW4, ROW5, ROW6, ROW7]


def setup_leds():
    """Configura los leds en modo salida"""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(columns, GPIO.OUT)
    GPIO.setup(rows, GPIO.OUT)


def leds_off():
    """Apaga todos los leds"""
    GPIO.output(columns, GPIO.HIGH)
    GPIO.output(rows, GPIO.HIGH)


setup_leds()


def show_j():
    # Para la J
    leds_off()
    GPIO.output(COL1, GPIO.HIGH)
    GPIO.output([ROW2, ROW3, ROW7], GPIO.LOW)
    sleep(0.1)
    leds_off()
    GPIO.output(COL2, GPIO.HIGH)
    GPIO.output([ROW1, ROW7], GPIO.LOW)
    sleep(0.1)
    leds_off()

    GPIO.output(COL3, GPIO.HIGH)
    GPIO.output([ROW1, ROW7], GPIO.LOW)
    sleep(0.1)
    leds_off()

    GPIO.output(COL4, GPIO.HIGH)
    GPIO.output([ROW1, ROW7], GPIO.LOW)
    sleep(0.1)
    leds_off()

    GPIO.output(COL5, GPIO.HIGH)
    GPIO.output([ROW2, ROW3, ROW4, ROW5, ROW6, ROW7], GPIO.LOW)
    sleep(0.1)
    leds_off()


def show_a():
    leds_off()
    GPIO.output(COL1, GPIO.HIGH)
    GPIO.output([ROW1, ROW2, ROW3, ROW4, ROW5, ROW6], GPIO.LOW)
    sleep(0.1)
    leds_off()
    GPIO.output(COL2, GPIO.HIGH)
    GPIO.output([ROW3, ROW7], GPIO.LOW)
    sleep(0.1)
    leds_off()
    GPIO.output(COL3, GPIO.HIGH)
    GPIO.output([ROW3, ROW7], GPIO.LOW)
    sleep(0.1)
    leds_off()
    GPIO.output(COL4, GPIO.HIGH)
    GPIO.output([ROW3, ROW7], GPIO.LOW)
    sleep(0.1)
    leds_off()
    GPIO.output(COL5, GPIO.HIGH)
    GPIO.output([ROW1, ROW2, ROW3, ROW4, ROW5, ROW6], GPIO.LOW)



def show_d():
    leds_off()
    GPIO.output(COL1, GPIO.HIGH)
    GPIO.output([ROW1, ROW2, ROW3, ROW4, ROW5, ROW6,ROW7], GPIO.LOW)
    sleep(0.1)
    leds_off()
    GPIO.output(COL2, GPIO.HIGH)
    GPIO.output([ROW1, ROW7], GPIO.LOW)
    sleep(0.1)
    leds_off()
    GPIO.output(COL3, GPIO.HIGH)
    GPIO.output([ROW1, ROW7], GPIO.LOW)
    sleep(0.1)
    leds_off()
    GPIO.output(COL4, GPIO.HIGH)
    GPIO.output([ROW1, ROW7], GPIO.LOW)
    sleep(0.1)
    leds_off()
    GPIO.output(COL5, GPIO.HIGH)
    GPIO.output([ROW1, ROW2, ROW3, ROW4, ROW5, ROW6], GPIO.LOW)
