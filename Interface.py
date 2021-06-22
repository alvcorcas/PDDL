import tkinter as tk
from tkinter import *
from State import *
from Action import *
from Heuristics import *
from Search import *


# El formato para las acciones es A-p2-p4;B-p4-p5;C-p1-p2;D-p1,p4,p5-p3;E-p5,p2-p3;F-p1,p4-p3
# Es decir NOMBRE-PRECOND-EFECTOS
# Para el estado inicial y objetivo, el formato es literales separados por coma


# CAMPU
# p1,p3,p4,p9
# p10,p11,p21
# A-p6-p18,p8;B-p4-p20,p14,p16;C-p18,p20-p5;D-p7,p3-p6;E-p1-p7,p2;F-p5-p10,p13;G-p9,p13,p12-p11,p19;H-p14,p8-p12;I-p2,p19,p16-p15;J-p15-p21
#[B, E, D, A, C, F, H, G, I, J]
#[E, D, B, A, H, C, F, G, I, J]


initial_state = []
target = []
actions = set()
data = []


def cargardata(data):

    data[0] = data[0].replace('\n', '')  # Eliminamos saltos de líneas
    data[1] = data[1].replace('\n', '')
    data[2] = data[2].replace('\n', '')
    data[0] = data[0].replace(' ', '')  # Trimamos las cadenas
    data[1] = data[1].replace(' ', '')
    data[2] = data[2].replace(' ', '')

    for i in data[0].split(","):
        initial_state.append(i)

    for i in data[1].split(","):
        target.append(i)

    for i in data[2].split(";"):

        action1 = Action(i.split("-")[0], set(), set())

        for j in i.split("-")[1].split(","):
            action1.preconditions.add(j)
        for j in i.split("-")[2].split(","):
            action1.effects.add(j)
        actions.add(action1)


def resultado():
    global initial_state
    global target
    global actions
    global data
    global text

    initial_state = []
    target = []
    actions = set()
    data = []

    x2 = entry2.get()
    x3 = entry3.get()
    x4 = entry4.get()

    #x2 = 'p1,p3,p4,p9'
    #x3 = 'p10,p11,p21'
    #x4 = 'A-p6-p18,p8;B-p4-p20,p14,p16;C-p18,p20-p5;D-p7,p3-p6;E-p1-p7,p2;F-p5-p10,p13;G-p9,p13,p12-p11,p19;H-p14,p8-p12;I-p2,p19,p16-p15;J-p15-p21'

    data.append(x2)
    data.append(x3)
    data.append(x4)
    
    cargardata(data)

    if (chk_state_prego.get()):
        if(chk_state_backwards.get()):
            text['text'] = backward_search_prego(
                State(initial_state), State(target), actions)
        else:
            text['text'] = forward_search_prego(
                State(initial_state), State(target), actions)
    else:
        if(chk_state_backwards.get()):
            text['text'] = backward_search_delta0(
                State(initial_state), State(target), actions)
        else:
            text['text'] = forward_search_delta0(
                State(initial_state), State(target), actions)


root = tk.Tk()
root.title('PDDL')
canvas1 = tk.Canvas(root, width=450, height=600)
canvas1.pack()


label2 = tk.Label(root, text='Initial state:')
label2.config(font=('helvetica', 10))
canvas1.create_window(50, 120, window=label2)
entry2 = tk.Entry(root)
entry2.place(x=20,
             y=150,
             width=400,
             height=30)

format2 = Label(root, text="FORMAT: p1,p2,p3")
format2.place(x=20, y=180)

label3 = tk.Label(root, text='Final state:')
label3.config(font=('helvetica', 10))
canvas1.create_window(50, 220, window=label3)

entry3 = tk.Entry(root)
entry3.place(x=20,
             y=250,
             width=400,
             height=30)

format3 = Label(root, text="FORMAT: p1,p2,p3")
format3.place(x=20, y=280)


label4 = tk.Label(root, text='Actions:')
label4.config(font=('helvetica', 10))
canvas1.create_window(40, 320, window=label4)

entry4 = tk.Entry(root)
entry4.place(x=20,
             y=350,
             width=400,
             height=30)

format4 = Label(
    root, text="FORMAT: A-p1,p2,p3-p4;B-p2-p5 (NAME-PRECONDITIONS-EFFECTS)")
format4.place(x=20, y=380)


chk_state_prego = BooleanVar()

chk_state_prego.set(True)  # set check state

chk_prego = Checkbutton(
    root, text='Choose the heuristic prego, otherwise ∆0 heuristic will be used', var=chk_state_prego)

chk_prego.place(x=20, y=420)


chk_state_backwards = BooleanVar()

chk_state_backwards.set(True)  # set check state

chk_backwards = Checkbutton(
    root, text='Choose backward search, otherwise forward search will be used', var=chk_state_backwards)

chk_backwards.place(x=20, y=440)


button1 = tk.Button(text='RUN', command=resultado, )
canvas1.create_window(40, 500, window=button1)


label5 = tk.Label(root, text='Solution:')
label5.config(font=('helvetica', 10))
canvas1.create_window(50, 550, window=label5)

text = Label(root, text="")
text.place(x=100, y=540)

root.mainloop()
