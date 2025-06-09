# ia/minimax.py

import copy
from utils.calculo_daño import calcular_danio

INFINITO = float('inf')

def evaluar_estado(ia, jugador):
    ps_ia = sum(p.ps_actual for p in ia.pokemons if not p.esta_debilitado())
    ps_jugador = sum(p.ps_actual for p in jugador.pokemons if not p.esta_debilitado())

    activo_ia = ia.activo
    activo_jugador = jugador.activo

    danio_potencial = 0

    for ataque in activo_ia.ataques:
        danio = calcular_danio(activo_ia, activo_jugador, ataque)
        danio_potencial = max(danio_potencial, danio)

    return (ps_ia - ps_jugador) + danio_potencial * 0.5


def generar_acciones(entrenador):
    return [{"tipo": "ataque", "eleccion": a} for a in entrenador.activo.ataques]

def aplicar_accion(ia, jugador, accion, es_ia):
    atacante = ia if es_ia else jugador
    defensor = jugador if es_ia else ia
    ataque = accion["eleccion"]
    daño = calcular_danio(atacante.activo, defensor.activo, ataque)
    defensor.activo.recibir_daño(daño)
    if defensor.activo.esta_debilitado():
        defensor.cambiar_pokemon()

def minimax(ia, jugador, prof, alfa, beta, turno_ia):
    if not ia.tiene_pokemons_vivos(): return -INFINITO
    if not jugador.tiene_pokemons_vivos(): return INFINITO
    if prof == 0: return evaluar_estado(ia, jugador)

    if turno_ia:
        max_eval = -INFINITO
        for acc in generar_acciones(ia):
            ia_c, jug_c = copy.deepcopy(ia), copy.deepcopy(jugador)
            aplicar_accion(ia_c, jug_c, acc, True)
            val = minimax(ia_c, jug_c, prof - 1, alfa, beta, False)
            max_eval = max(max_eval, val)
            alfa = max(alfa, val)
            if beta <= alfa: break
        return max_eval
    else:
        min_eval = INFINITO
        for acc in generar_acciones(jugador):
            ia_c, jug_c = copy.deepcopy(ia), copy.deepcopy(jugador)
            aplicar_accion(ia_c, jug_c, acc, False)
            val = minimax(ia_c, jug_c, prof - 1, alfa, beta, True)
            min_eval = min(min_eval, val)
            beta = min(beta, val)
            if beta <= alfa: break
        return min_eval
