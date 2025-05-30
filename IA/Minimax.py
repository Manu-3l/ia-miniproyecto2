# ia/minimax.py

import copy
from utils.calculo_daño import calcular_danio

INFINITO = float('inf')

def evaluar_estado(ia, jugador):
    ps_ia = sum(p.ps_actual for p in ia.pokemons)
    ps_jugador = sum(p.ps_actual for p in jugador.pokemons)

    activo_ia = ia.activo
    activo_jugador = jugador.activo

    puntuacion = (ps_ia - ps_jugador)

    for ataque in activo_ia.ataques:
        daño_potencial = calcular_danio(activo_ia, activo_jugador, ataque)
        if daño_potencial >= activo_jugador.ps_actual:
            puntuacion += 200

    for ataque in activo_jugador.ataques:
        daño_potencial = calcular_danio(activo_jugador, activo_ia, ataque)
        if daño_potencial >= activo_ia.ps_actual:
            puntuacion -= 200

    return puntuacion

def generar_acciones(entrenador):
    return [{"tipo": "ataque", "eleccion": ataque} for ataque in entrenador.activo.ataques]

def minimax(ia, jugador, profundidad, alfa, beta, es_turno_ia):
    if not ia.tiene_pokemons_vivos():
        return -INFINITO
    if not jugador.tiene_pokemons_vivos():
        return INFINITO
    if profundidad == 0:
        return evaluar_estado(ia, jugador)

    if es_turno_ia:
        max_eval = -INFINITO
        for accion in generar_acciones(ia):
            ia_copia, jugador_copia = copy.deepcopy(ia), copy.deepcopy(jugador)
            aplicar_accion(ia_copia, jugador_copia, accion, True)
            eval = minimax(ia_copia, jugador_copia, profundidad - 1, alfa, beta, False)
            max_eval = max(max_eval, eval)
            alfa = max(alfa, eval)
            if beta <= alfa:
                break
        return max_eval
    else:
        min_eval = INFINITO
        for accion in generar_acciones(jugador):
            ia_copia, jugador_copia = copy.deepcopy(ia), copy.deepcopy(jugador)
            aplicar_accion(ia_copia, jugador_copia, accion, False)
            eval = minimax(ia_copia, jugador_copia, profundidad - 1, alfa, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alfa:
                break
        return min_eval

def aplicar_accion(ia, jugador, accion, es_turno_ia):
    atacante = ia if es_turno_ia else jugador
    defensor = jugador if es_turno_ia else ia

    ataque = accion["eleccion"]
    daño = calcular_danio(atacante.activo, defensor.activo, ataque)
    defensor.activo.recibir_daño(daño)

    if defensor.activo.esta_debilitado():
        defensor.cambiar_pokemon()
