from tkinter import Button, Canvas, Tk, PhotoImage
import Lab5 as lab


def show_j():
    print("Debe mmotrar la J")
    img = PhotoImage(file="letter_J.png")
    c.create_image(100, 120, anchor="center", image=img)
    c.img = img


def show_a():
    print("Debe mmotrar la A")
    img = PhotoImage(file="letter_A.png")
    c.create_image(110, 120, anchor="center", image=img)
    c.img = img


def show_d():
    
    print("Debe mmotrar la D")
    img = PhotoImage(file="letter_D.png")
    c.create_image(100, 120, anchor="center", image=img)
    c.img = img


ventana = Tk()
ventana.geometry("400x300")
ventana.title("Laboratorio 5!")
c = Canvas(ventana, width=600, height=600)
c.place(x=150, y=20)
Button(ventana, text="Mostrar la J", command=show_j).place(x=20, y=20)
Button(ventana, text="Mostrar la A", command=show_a).place(x=20, y=60)
Button(ventana, text="Mostrar la D", command=show_d).place(x=20, y=100)
Button(ventana, text="Salir", command=ventana.quit).place(x=20, y=200)
ventana.mainloop()
