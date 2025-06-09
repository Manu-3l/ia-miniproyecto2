# modelo/combate.py

from utils.calculo_daño import calcular_danio

class Combate:
    def __init__(self, jugador, ia):
        self.jugador = jugador
        self.ia = ia
        self.turno = 1

    def ejecutar_turno(self, ataque_jugador, ataque_ia):
        poke_jugador = self.jugador.activo
        poke_ia = self.ia.activo

        primero, segundo = (self.jugador, self.ia) if poke_jugador.get_estadistica("velocidad") >= poke_ia.get_estadistica("velocidad") else (self.ia, self.jugador)
        acciones = {self.jugador: ataque_jugador, self.ia: ataque_ia}

        for entrenador in [primero, segundo]:
            atacante = entrenador.activo
            defensor = self.ia.activo if entrenador == self.jugador else self.jugador.activo
            ataque = acciones[entrenador]

            if atacante.esta_debilitado():
                continue

            daño = calcular_danio(atacante, defensor, ataque)
            defensor.recibir_daño(daño)
            print(f"{atacante.nombre} usa {ataque.nombre} e inflige {daño} de daño a {defensor.nombre} (PS: {defensor.ps_actual}/{defensor.ps_max})")

            if defensor.esta_debilitado():
                print(f"{defensor.nombre} ha sido debilitado!")
                return "debilitado"



        self.turno += 1
        return "continuar"
