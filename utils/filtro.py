from utils.tipos_movesets import MOVIMIENTOS_PERMITIDOS_POR_TIPO

def puede_aprender(pokemon, ataque):
    tipos = set()
    if pokemon.tipo1 in MOVIMIENTOS_PERMITIDOS_POR_TIPO:
        tipos.update(MOVIMIENTOS_PERMITIDOS_POR_TIPO[pokemon.tipo1])
    if pokemon.tipo2 in MOVIMIENTOS_PERMITIDOS_POR_TIPO:
        tipos.update(MOVIMIENTOS_PERMITIDOS_POR_TIPO[pokemon.tipo2])

    if ataque.tipo not in tipos:
        return False
    if ataque.categoria == "fisico" and ataque.poder > 70 and ataque.poder < 100 and pokemon.get_estadistica("ataque") < 70:
        return False
    if ataque.categoria == "especial" and ataque.poder > 70 and ataque.poder < 100 and pokemon.get_estadistica("ataque especial") < 70:
        return False
    if ataque.categoria == "fisico" and ataque.poder >= 100 and pokemon.get_estadistica("ataque") < 80:
        return False
    if ataque.categoria == "especial" and ataque.poder >= 100 and pokemon.get_estadistica("ataque especial") < 80:
        return False
    return True

def filtrar_movimientos(pokemon, lista_ataques):
    return [a for a in lista_ataques if puede_aprender(pokemon, a)]
