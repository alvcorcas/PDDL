import tkinter as tk
from tkinter import *
from State import *
from Action import *
from prego import *


# El formato para las acciones es A-p2-p4;B-p4-p5;C-p1-p2;D-p1,p4,p5-p3;E-p5,p2-p3;F-p1,p5-p3
# Es decir NOMBRE-PRECOND-EFECTOS
# Para el estado inicial y objetivo, el formato es literales separados por coma


initialstate = State([])
objective = []
actions = []
datos = []



def cargardatos(datos):

        datos[0] = datos[0].replace('\n', '')
        datos[1] = datos[1].replace('\n', '')
        datos[2] = datos[2].replace('\n', '')

        
        for i in datos[0].split(","):
                initialstate.literals.append(i)

        for i in datos[1].split(","):
                objective.append(i)

        for i in datos[2].split(";"):

                action1 = Action(i.split("-")[0], [], [])

                for j in i.split("-")[1].split(","):
                        action1.preconditions.append(j)
                for j in i.split("-")[2].split(","):
                        action1.effects.append(j)
                actions.append(action1)


       


def resultado():
        global initialstate
        global objective
        global actions
        global datos
        initialstate = State([])
        objective = []
        actions = []
        datos = []
        x2 = entry2.get()
        x3 = entry3.get()
        x4 = entry4.get()
        datos.append(x2)
        datos.append(x3)
        datos.append(x4)
        cargardatos(datos)

        if (chk_state_prego.get()):

                text = Label(root, text=prego(initialstate,objective,actions))   
                text.place(x=100,y=540)
        else:
                text = Label(root, text=delta0(initialstate,objective,actions))   
                text.place(x=100,y=540)
    

        
    


root= tk.Tk()
canvas1 = tk.Canvas(root, width = 450, height = 600)
canvas1.pack()


label2 = tk.Label(root, text='Initial state:')
label2.config(font=('helvetica', 10))
canvas1.create_window(50, 120, window=label2)
entry2 = tk.Entry (root) 
entry2.place(x = 20,
        y = 150,
        width=400,
        height=30)


label3 = tk.Label(root, text='Final state:')
label3.config(font=('helvetica', 10))
canvas1.create_window(50, 220, window=label3)

entry3 = tk.Entry (root) 
entry3.place(x = 20,
        y = 250,
        width=400,
        height=30)


label4 = tk.Label(root, text='Actions:')
label4.config(font=('helvetica', 10))
canvas1.create_window(40, 320, window=label4)

entry4 = tk.Entry (root) 
entry4.place(x = 20,
        y = 350,
        width=400,
        height=30)


chk_state_prego = BooleanVar()

chk_state_prego.set(True) #set check state

chk_prego = Checkbutton(root, text='Choose the heuristic prego // Si no se marca, se utilizará ∆0', var=chk_state_prego)

chk_prego.place(x=20, y=400)


    
button1 = tk.Button(text='RUN', command=resultado, )
canvas1.create_window(40, 500, window=button1)


label5 = tk.Label(root, text='Solution:')
label5.config(font=('helvetica', 10))
canvas1.create_window(50, 550, window=label5)

root.mainloop()




