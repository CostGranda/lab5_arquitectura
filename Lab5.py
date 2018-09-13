from abcdario import show_g, show_a, show_n, show_d, show_r, clean, leds_off, show_l, show_z, show_c, show_o, show_j, show_s, setup_pin
from time import sleep

setup_pin()


def show_granda():
    try:
        for i in range(2):
            leds_off()
            show_g()
            sleep(0.1)
            leds_off()
            show_r()
            sleep(0.1)
            leds_off()
            show_a()
            sleep(0.1)
            leds_off()
            show_n()
            sleep(0.1)
            leds_off()
            show_d()
            sleep(0.1)
            leds_off()
            show_a()
            sleep(0.1)
            leds_off()
    except KeyboardInterrupt:
        clean()


def show_alcaraz():
    try:
        for i in range(2):
            leds_off()
            show_a()
            sleep(0.1)
            leds_off()
            show_l()
            sleep(0.1)
            leds_off()
            show_c()
            sleep(0.1)
            leds_off()
            show_a()
            sleep(0.1)
            leds_off()
            show_r()
            sleep(0.1)
            leds_off()
            show_a()
            sleep(0.1)
            leds_off()
            show_z()
            sleep(0.1)
            leds_off()
    except KeyboardInterrupt:
        clean()


def show_rojas():
    try:
        for i in range(2):
            leds_off()
            show_r()
            sleep(0.1)
            leds_off()
            show_o()
            sleep(0.1)
            leds_off()
            show_j()
            sleep(0.1)
            leds_off()
            show_a()
            sleep(0.1)
            leds_off()
            show_s()
            sleep(0.1)
            leds_off()
    except KeyboardInterrupt:
        clean()