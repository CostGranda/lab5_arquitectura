import tkinter as tk
from abcdario import show_g, show_a, show_n, show_d, show_r, clean, leds_off, show_l, show_z, show_c, show_o, show_j, show_s, setup_pin
import tkinter.font
from time import sleep
#import Lab5 


root = tk.Tk()
root.geometry("1200x900")
root.title("apellidos MATRIZ DE LEDS")
fuente=tkinter.font.Font(family='helvetica',size=20,weight="bold")
fuente2=tkinter.font.Font(family='helvetica',size=12,weight ="bold")
fuente3=tkinter.font.Font(family='helvetica',size=120,weight ="bold")

integrantes = """
Andrés Alcaraz    ???
David Rojas       1017248534
Jorge Luis Granda 1042770436

Ingeniero Hernando Vanegas López
"""
label = tk.Label(text=integrantes,font=fuente,bg="#000000",fg="#F4845F")

label.pack(fill=tk.X)

granda = {"G":show_g, "R": show_r,"A": show_a, "N":show_n, "D":show_d, "A":show_a}

def btn_granda():
  apellido_granda= ['G','R','A','N','D','A','']
  for letra in apellido_granda:
    lbl_resultado['text']= letra
    sleep(0.1)
    root.update_idletasks()
    granda[letra]()
    leds_off()

alcaraz = {"A":show_a, "L": show_l,"C": show_c, "A":show_a, "R":show_r, "A":show_a, "Z": show_z}

def btn_alcaraz():
  apellido_alcaraz = ['A','L','C','A','R','A','Z', '']
  for letra in apellido_alcaraz:
    lbl_resultado['text']=letra
    sleep(0.1)
    root.update_idletasks()
    alcaraz[letra]()
    leds_off()

rojas = {"R": show_r, "O": show_o, "J": show_j, "A": show_a, "S": show_s}
def btn_rojas():
  apellido_rojas = ['R','O','J','A','S','']
  for letra in apellido_rojas:
    lbl_resultado['text']=letra
    sleep(1)
    root.update_idletasks()
    rojas[letra]()
    leds_off()


def generar():
  px=50
  py=210
  label = ['G','R','A','N','D','A','L','C','R','Z','O','J','S']
  apellidos='GRANDALCRZOJS'
  a=0
  for letra in apellidos:
    label[a]= tk.Button(text = letra,font=fuente2, bd=5)
    label[a].place(x=px,y=py,height=70, width=70)
    px=px+100
    if(a==5):
      px=50
      py=py+100
    elif(a==9):
      px=50
      py=py+100
    a=a+1


generar()

lbl_resultado=tk.Label(root,text="",font=fuente3,bg="#000000",fg="#F27059")
lbl_resultado.place(x=850,y=200,height=400,width=400)
boton_nombre=tk.Button(text="GRANDA",command=btn_granda, bd=4)
boton_nombre.place(x=850,y=600,height=60,width=70)
boton_apellido1=tk.Button(text="ALCARAZ",command=btn_alcaraz, bd=4)
boton_apellido1.place(x=950,y=600,height=60,width=90)
boton_apellido2=tk.Button(text="ROJAS",command=btn_rojas,bd=4)
boton_apellido2.place(x=1050,y=600,height=60,width=100)

root.mainloop()