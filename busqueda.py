FUNCION BUSQUEDA-EN-PROFUNDIDAD-H(ESTADO-INICIAL,OBJETIVO,ACCIONES)
    Devolver BEP-H-REC({},{},ESTADO-INICIAL,OBJETIVO,ACCIONES)

FUNCION BEP-H-REC(PLAN,VISITADOS,ACTUAL,OBJ,ACCIONES)
     Si ACTUAL satisface OBJ, devolver PLAN
     Hacer APLICABLES igual a la lista de acciones que sean instancias
     una acción de ACCIONES, que sean aplicables a ACTUAL y cuya
    aplicación no resulte en un estado de VISITADOS
     Hacer ORD-APLICABLES igual a ORDENA-POR-HEURISTICA(APLICABLES)
     Para cada ACCION en ORD-APLICABLES
    Hacer E’ el resultado de aplicar ACCION a ACTUAL
    Hacer RES igual a
    H-REC(PLAN·ACCION,VISITADOS U {E’},E’,OBJ,ACCIONES)
    Si RES no es FALLO, devolver RES y terminar
     Devolver FALLO