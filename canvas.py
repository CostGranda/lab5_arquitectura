from tkinter import Button, Canvas, Tk, PhotoImage
import Lab5 as lab
from threading import Thread, Event
from time import sleep

threads = list()


def show_j():
    event.wait()
    print("Debe mmotrar la J")
    img = PhotoImage(file="letter_J.png")
    c.create_image(100, 120, anchor="center", image=img)
    c.img = img
    i = 0
    try:
        while i<3:
            print("Esto es una secuencia de J")
            sleep(5)
            i+=1
    except KeyboardInterrupt:
        print("Detenido")
    event.clear()


def show_a():
    event.wait()
    print("Debe mmotrar la A")
    img = PhotoImage(file="letter_A.png")
    c.create_image(110, 120, anchor="center", image=img)
    c.img = img
    i=0
    try:
        while i<3:
            print("Esto es una secuencia de A")
            sleep(5)
            i+=1
    except KeyboardInterrupt:
        print("Detenido")
    event.clear()
    a._delete()



def show_d():
    event.wait()
    print("Debe mmotrar la D")
    img = PhotoImage(file="letter_D.png")
    c.create_image(100, 120, anchor="center", image=img)
    c.img = img
    i=0
    try:
        while i<3:
            print("Esto es una secuencia de D")
            sleep(5)
            i+=1
    except KeyboardInterrupt:
        print("Detenido")
    event.clear()
    d._delete()


def hilo_exit():
    MAIN_WINDOW.quit()


MAIN_WINDOW = Tk()
MAIN_WINDOW.geometry("400x300")
MAIN_WINDOW.title("Laboratorio 5!")
c = Canvas(MAIN_WINDOW, width=600, height=600)
c.place(x=150, y=20)

event = Event()

j = Thread(target=show_j, name='J')
a = Thread(target=show_a, name='A')
d = Thread(target=show_d, name='D')

def hilo_j():
    if not event.is_set():
        event.set()
        j.start()
def hilo_a():
    if not event.is_set():
        event.set()
        a.start()
def hilo_d():
    if not event.is_set():
        event.set()
        d.start()


Button(MAIN_WINDOW, text="Mostrar la J", command=hilo_j).place(x=20, y=20)
Button(MAIN_WINDOW, text="Mostrar la A", command=hilo_a).place(x=20, y=60)
Button(MAIN_WINDOW, text="Mostrar la D", command=hilo_d).place(x=20, y=100)
Button(MAIN_WINDOW, text="Salir", command=hilo_exit).place(x=20, y=200)
MAIN_WINDOW.mainloop()
