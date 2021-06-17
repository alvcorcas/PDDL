from Action import *

A = Action("A", ['p2'], ['p4'])
B = Action("B", ['p4'], ['p5'])
C = Action("C", ['p6'], ['p5'])
D = Action("D", ['p1', 'p4', 'p5'], ['p3', 'p7'])

acciones = [A, B, C, D]
print(acciones)
