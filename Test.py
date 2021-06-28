import Backward_search as bs
import Forward_search as fs
from Action import Action
from State import State
import time as tm

# A = Action("A", {'p1', 'p2'}, {'p7'})
# B = Action("B", {'p3', 'p4', 'p5'}, {'p8'})
# C = Action("C", {'p6'}, {'p9'})
# D = Action("D", {'p10'}, {'p11', 'p12'})
# E = Action("E", {'p11'}, {'p13'})
# F = Action("F", {'p12'}, {'p14'})
# G = Action("G", {'p23'}, {'p26'})
# H = Action("H", {'p22'}, {'p24', 'p25'})
# I = Action("I", {'p21'}, {'p18'})
# J = Action("J", {'p13', 'p14'}, {'p15'})
# K = Action("K", {'p7', 'p9'}, {'p10'})
# L = Action("L", {'p8'}, {'p16'})
# M = Action("M", {'p15', 'p16'}, {'p17'})
# N = Action("N", {'p17'}, {'p18', 'p19', 'p20'})
# O = Action("O", {'p17'}, {'p21'})
# P = Action("P", {'p17'}, {'p22', 'p23', 'p21'})
# Q = Action("Q", {'p24', 'p26'}, {'p27'})
# R = Action("R", {'p27', 'p18'}, {'p28'})
# S = Action("S", {'p25'}, {'p29'})
# T = Action("T", {'p28', 'p29'}, {'p30'})
# U = Action("U", {'p30'}, {'p31', 'p32', 'p33'})
# V = Action("V", {'p32'}, {'p34'})
# W = Action("W", {'p30'}, {'p35', 'p32'})
# X = Action("X", {'p33'}, {'p36'})
# Y = Action("Y", {'p31'}, {'p37'})
# Z = Action("Z", {'p34', 'p36', 'p37'}, {'p40'})
# A_1 = Action("A_1", {'p35', 'p32'}, {'p40'})

# initial_state = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6']
# target = ['p29', 'p27', 'p18']
# actions = {A, B, C, D, E, F, G, H, I, J, K,
#            L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A_1}


# print()
# print('\nHacia atrás prego:')
# time0 = tm.time()
# print(search.backward_search_prego(State(initial_state), State(target), actions))
# time1 = tm.time()
# print(f'Tiempo: {time1 - time0}')

# print('\nHacia delante prego:')
# time2 = tm.time()
# print(search.forward_search_prego(State(initial_state), State(target), actions))
# time3 = tm.time()
# print(f'Tiempo: {time3 - time2}')

# print('\nHacia delante delta0:')
# time6 = tm.time()
# print(search.forward_search_delta0(State(initial_state), State(target), actions))
# time7 = tm.time()
# print(f'Tiempo: {time7 - time6}')

# print('\nHacia atrás delta0:')
# time4 = tm.time()
# print(search.backward_search_delta0(State(initial_state), State(target), actions))
# time5 = tm.time()
# print(f'Tiempo: {time5 - time4}')


# print()


# path = [A, B, L, C, K, D, E, F, J, M]
# visited = [State(['p3', 'p4', 'p2', 'p5', 'p1', 'p6', 'p7']),
#           State(['p3', 'p4', 'p2', 'p5', 'p1', 'p6', 'p8', 'p7']),
#           State(['p3', 'p4', 'p2', 'p8', 'p16', 'p5', 'p1', 'p6', 'p7']),
#           State(['p3', 'p4', 'p2', 'p8', 'p16', 'p9', 'p5', 'p1', 'p6', 'p7']),
#           State(['p3', 'p4', 'p2', 'p10', 'p8',
#                 'p16', 'p9', 'p5', 'p1', 'p6', 'p7']),
#           State(['p3', 'p4', 'p2', 'p10', 'p8', 'p16', 'p9',
#                  'p11', 'p5', 'p1', 'p12', 'p6', 'p7']),
#           State(['p3', 'p4', 'p2', 'p10', 'p8', 'p16', 'p9',
#                  'p11', 'p5', 'p1', 'p12', 'p13', 'p6', 'p7']),
#           State(['p3', 'p4', 'p2', 'p10', 'p8', 'p16', 'p9', 'p11',
#                  'p5', 'p1', 'p12', 'p13', 'p6', 'p7', 'p14']),
#           State(['p3', 'p4', 'p2', 'p10', 'p15', 'p8', 'p16', 'p9',
#                  'p11', 'p5', 'p1', 'p12', 'p13', 'p6', 'p7', 'p14']),
#           State(['p4', 'p16', 'p11', 'p12', 'p13', 'p6', 'p7', 'p3', 'p2', 'p10', 'p15', 'p8', 'p9', 'p5', 'p1', 'p17', 'p14'])]
# current = ['p4', 'p16', 'p11', 'p12', 'p13', 'p6', 'p7', 'p3',
#           'p2', 'p10', 'p15', 'p8', 'p9', 'p5', 'p1', 'p17', 'p14']

# print(forward_search_prego_aux(path, visited,
#                               State(current), State(target), actions))


# s1 = State(['p1', 'p3', 'p5'])
# visiteds = [State(['p1', 'p3'])]
# print(s1.not_in(visiteds))

actions = set()


def conexion_entre(hab1, hab2):
    actions.add(Action(f"ir({hab1},{hab2})", {
                f'en({hab1})', f'abierta({hab1},{hab2})'}, set(), {f'en({hab2})'}, {f'en({hab1})'}))
    actions.add(Action(f"abrir_puerta({hab1},{hab2})", {f'en({hab1})'}, {
                f'abierta({hab1},{hab2})'}, {f'abierta({hab1},{hab2})'}, set()))


conexion_entre('A', 'B')
conexion_entre('A', 'C')
conexion_entre('B', 'D')
conexion_entre('C', 'E')
conexion_entre('C', 'F')
conexion_entre('D', 'E')
conexion_entre('D', 'F')
conexion_entre('E', 'Z')

literals = ['en(A)', 'abierta(A,B)', 'abierta(C,E)', 'abierta(C,F)', 'abierta(D,F)', 'abierta(E,Z)'
            ]

initial_state = State(literals)

target = State(['en(Z)'])

print('\nHacia delante ciega:')
time6 = tm.time()
print(fs.forward_search_blind(initial_state, target, actions))
time7 = tm.time()
print(f'Tiempo: {time7 - time6}')

print('\nHacia atrás ciega:')
time4 = tm.time()
print(bs.backward_search_blind(initial_state, target, actions))
time5 = tm.time()
print(f'Tiempo: {time5 - time4}')

print()