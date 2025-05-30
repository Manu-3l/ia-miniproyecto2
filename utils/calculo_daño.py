# utils/calculo_danio.py

from utils.Efectividades import EFECTIVIDADES

def calcular_danio(atacante, defensor, ataque):
    if ataque.categoria == "fisico":
        ataque_stat = atacante.get_estadistica("ataque")
        defensa_stat = defensor.get_estadistica("defensa")
    elif ataque.categoria == "especial":
        ataque_stat = atacante.get_estadistica("ataque especial")
        defensa_stat = defensor.get_estadistica("defensa especial")
    else:
        return 0

    nivel = atacante.nivel
    poder = ataque.poder
    efectividad = EFECTIVIDADES.get((ataque.tipo, defensor.tipo1), 1.0)
    if defensor.tipo2:
        efectividad *= EFECTIVIDADES.get((ataque.tipo, defensor.tipo2), 1.0)

    daño = (((2 * nivel / 5 + 2) * poder * (ataque_stat / defensa_stat)) / 50 + 2) * efectividad
    return max(1, int(daño))
