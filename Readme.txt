El código esta estructurado en 3 partes:
-Interfaz.py, código fuente de la interfaz y tratamiento de los datos de entrada para construir los objetos.
-Heuristics.py, se encuentra el código fuente que implementan las diferentes heurísticas.
-State.py, Action.py, son las clases que modelan el problema.
-Backward_search.py, se encuentra el código fuente que implemente la técnica de búsqueda hacia atrás.
-Forward_search.py, se encuentra el código fuente que implemente la técnica de búsqueda hacia delante.

Datos de un problema para introducir en la interfaz:
Basta con rellenar los diferentes campos de la interfaz, elegir la heurística,técnica y pulsar sobre RUN

-Initial state:en(A) abierta(A,B) abierta(C,E) abierta(C,F) abierta(D,F) abierta(E,Z)

-Final state:en(Z)

-Actions: abrir_puerta(A,B)-en(A)-abierta(A,B)-abierta(A,B)-;abrir_puerta(B,D)-en(B)-abierta(B,D)-abierta(B,D)-;ir(D,E)-abierta(D,E) en(D)--en(E)-en(D);abrir_puerta(E,Z)-en(E)-abierta(E,Z)-abierta(E,Z)-;ir(B,D)-abierta(B,D) en(B)--en(D)-en(B);ir(A,C)-abierta(A,C) en(A)--en(C)-en(A);abrir_puerta(C,F)-en(C)-abierta(C,F)-abierta(C,F)-;ir(E,Z)-en(E) abierta(E,Z)--en(Z)-en(E);ir(C,F)-en(C) abierta(C,F)--en(F)-en(C);abrir_puerta(A,C)-en(A)-abierta(A,C)-abierta(A,C)-;abrir_puerta(D,F)-en(D)-abierta(D,F)-abierta(D,F)-;ir(A,B)-en(A) abierta(A,B)--en(B)-en(A);abrir_puerta(C,E)-en(C)-abierta(C,E)-abierta(C,E)-;ir(D,F)-abierta(D,F) en(D)--en(F)-en(D);ir(C,E)-en(C) abierta(C,E)--en(E)-en(C);abrir_puerta(D,E)-en(D)-abierta(D,E)-abierta(D,E)-;

-Resultado esperado: abrir_puerta(A, C) ir(A, C) ir(C, E) ir(E, Z) 