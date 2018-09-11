from tkinter import * 

ventana = Tk()
c = Canvas(ventana, width=500,height=500)
ventana.geometry("600x600")
c.pack()
img = PhotoImage(file="letter_A.png")
c.create_image(100,100, anchor=NW, image=img)
ventana.mainloop()
