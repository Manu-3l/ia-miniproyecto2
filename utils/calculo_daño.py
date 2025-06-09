# utils/calculo_danio.py

from utils.Efectividades import EFECTIVIDADES

def calcular_danio(atacante, defensor, ataque):
    if ataque.categoria == "fisico":
        atq = atacante.get_estadistica("ataque")
        dfs = defensor.get_estadistica("defensa")
    else:
        atq = atacante.get_estadistica("ataque especial")
        dfs = defensor.get_estadistica("defensa especial")

    poder = ataque.poder
    nivel = atacante.nivel

    efectividad = EFECTIVIDADES.get((ataque.tipo, defensor.tipo1), 1.0)
    if defensor.tipo2:
        efectividad *= EFECTIVIDADES.get((ataque.tipo, defensor.tipo2), 1.0)

    daño = (((2 * nivel / 5 + 2) * poder * (atq / dfs)) / 50 + 2) * efectividad
    return max(1, int(daño))
