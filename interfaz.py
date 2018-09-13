import tkinter as tk
from abcdario import show_g, show_a, show_n, show_d, show_r, clean, leds_off, show_l, show_z, show_c, show_o, show_j, show_s, setup_pin
import tkinter.font
from time import sleep
import Lab5 


root = tk.Tk()
root.geometry("2000x900")
root.title("APELLIDOS MATRIZ DE LEDS")
fuente=tkinter.font.Font(family='helvetica',size=20,weight="bold")
fuente2=tkinter.font.Font(family='helvetica',size=12,weight ="bold")
fuente3=tkinter.font.Font(family='helvetica',size=120,weight ="bold")

integrantes = """
Andrés Alcaraz    ???
David Rojas       1017248534
Jorge Luis Granda 1042770436
"""
label = tk.Label(text="Nombre: Alexander Quintero Rosso 1037645440 \n" +
"       Sebastian Rivera Giraldo\n"+
"      Ramiro Andres Bedoya Gallon\n"+
"Ingeniero Hernando Vanegas López\n "+
"Matriz de leds",font=fuente,bg="#000000",fg="#007ACC")

label.pack(fill=tk.X)


def btn_granda():
  apellido_quintero= ['Q','U','I','N','T','E','R','O','']
  for i in range(0,9,1):
    lbl_resultado['text']=apellido_quintero[i]
    sleep(1)
    root.update_idletasks()
  


def btn_alcaraz():
  apellido_rivera = ['R','I','V','E','R','A','']
  for i in range(0,7,1):
    lbl_resultado['text']=apellido_rivera[i]
    sleep(1)
    root.update_idletasks()


def btn_rojas():
  apellido_bedoya = ['B','E','D','O','Y','A','']
  for i in range(0,7,1):
    lbl_resultado['text']=apellido_bedoya[i]
    sleep(1)
    root.update_idletasks()


def generar():
  px=50
  py=200
  label = ['Q','U','I','N','T','E','R','O','V','A','B','D','Y']
  Apellidos='QUINTEROVABDY'
  a=0
  for letra in Apellidos:
    label[a]= tk.Button(text = letra,font=fuente2)
    label[a].place(x=px,y=py,height=70, width=70)
    px=px+100
    if(a==7):
      px=50
      py=py+100
    elif(a==9):
      px=50
      py=py+100
    a=a+1


generar()

lbl_resultado=tk.Label(root,text="",font=fuente3,bg="#000000",fg="#007ACC")
lbl_resultado.place(x=850,y=200,height=400,width=400)
boton_nombre=tk.Button(text="QUINTERO",command=btn_granda)
boton_nombre.place(x=850,y=600,height=60,width=70)
boton_apellido1=tk.Button(text="RIVERA",command=btn_alcaraz)
boton_apellido1.place(x=950,y=600,height=60,width=90)
boton_apellido2=tk.Button(text="BEDOYA",command=btn_rojas)
boton_apellido2.place(x=1050,y=600,height=60,width=100)

root.mainloop()