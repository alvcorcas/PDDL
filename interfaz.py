import tkinter as tk
from tkinter import *

datos= []

root= tk.Tk()
canvas1 = tk.Canvas(root, width = 450, height = 600)
canvas1.pack()

label1 = tk.Label(root, text='States:')
label1.config(font=('helvetica', 10))
canvas1.create_window(40, 70, window=label1)


entry1 = tk.Entry (root) 
entry1.place(x = 20,
        y = 100,
        width=400,
        height=30)


label2 = tk.Label(root, text='Initial state:')
label2.config(font=('helvetica', 10))
canvas1.create_window(50, 170, window=label2)
entry2 = tk.Entry (root) 
entry2.place(x = 20,
        y = 200,
        width=400,
        height=30)



label3 = tk.Label(root, text='Final state:')
label3.config(font=('helvetica', 10))
canvas1.create_window(50, 270, window=label3)

entry3 = tk.Entry (root) 
entry3.place(x = 20,
        y = 300,
        width=400,
        height=30)


label4 = tk.Label(root, text='Actions:')
label4.config(font=('helvetica', 10))
canvas1.create_window(40, 370, window=label4)

entry4 = tk.Entry (root) 
entry4.place(x = 20,
        y = 400,
        width=400,
        height=30)


def getSquareRoot ():  
    x1 = entry1.get()
    x2 = entry2.get()
    x3 = entry3.get()
    x4 = entry4.get()
    datos.append(x1)
    datos.append(x2)
    datos.append(x3)
    datos.append(x4)

    
button1 = tk.Button(text='RUN', command=getSquareRoot)
canvas1.create_window(40, 500, window=button1)

root.mainloop()
print(datos[0])
print(datos[1])
print(datos[2])
print(datos[3])