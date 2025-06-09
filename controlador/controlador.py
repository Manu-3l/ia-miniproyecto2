# controlador/combate_controller.py

import copy
from IA.Minimax import generar_acciones, aplicar_accion, minimax, evaluar_estado
import copy
from modelo.Combate import calcular_danio



class Controlador:
    def __init__(self, jugador, ia, vista, combate):
        self.jugador = jugador
        self.ia = ia
        self.vista = vista
        self.combate = combate
        self.vista.actualizar_sprite("jugador", self.jugador.activo.nombre)
        self.vista.actualizar_sprite("ia", self.ia.activo.nombre)


        # Enlazar acción de ataque del jugador
        self.vista.on_ataque = self.turno_jugador
        self.vista.actualizar_botones(self.jugador.activo.ataques)
        self.vista.agregar_log("¡Combate iniciado!")

    def cambiar_pokemon_jugador(self, indice_local):
        vivos = [p for p in self.jugador.pokemons if not p.esta_debilitado()]
        nuevo = vivos[indice_local]
        self.jugador.indice_activo = self.jugador.pokemons.index(nuevo)
        self.vista.agregar_log(f"{nuevo.nombre} entra al combate.")
        self.vista.actualizar_botones(nuevo.ataques)
        self.vista.activar_botones_ataque()
        self.vista.actualizar_sprite("jugador", self.jugador.activo.nombre)
        


    def _desactivar_botones(self):
        for b in self.vista.botones:
            b["state"] = "disabled"

    def turno_jugador(self, idx):
        ataque_j = self.jugador.activo.ataques[idx]

        # IA elige
        acciones_ia = generar_acciones(self.ia)
        mejor_valor = float('-inf')
        mejor_accion = None

        for accion in acciones_ia:
            copia_ia = copy.deepcopy(self.ia)
            copia_jugador = copy.deepcopy(self.jugador)
            aplicar_accion(copia_ia, copia_jugador, accion, es_ia=True)
            valor = minimax(copia_ia, copia_jugador, 2, -float("inf"), float("inf"), False)
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_accion = accion

        ataque_ia = mejor_accion["eleccion"]



        # Mostrar movimientos
        self.vista.agregar_log(f"Jugador: {self.jugador.activo.nombre} usa {ataque_j.nombre}")
        self.vista.agregar_log(f"IA: {self.ia.activo.nombre} usa {ataque_ia.nombre}")

        estado = self.combate.ejecutar_turno(ataque_j, ataque_ia)

        self.vista.agregar_log(f"Jugador: {self.jugador.activo.nombre} PS: {self.jugador.activo.ps_actual}")
        self.vista.agregar_log(f"IA: {self.ia.activo.nombre} PS: {self.ia.activo.ps_actual}")

        if estado == "debilitado":
            # Verifica si el jugador fue debilitado
            if self.jugador.activo.esta_debilitado():
                if not self.jugador.tiene_pokemons_vivos():
                    self.vista.agregar_log("¡Has perdido el combate!")
                    self._desactivar_botones()
                    return
                vivos = [p for p in self.jugador.pokemons if not p.esta_debilitado()]
                self.vista.desactivar_botones_ataque()
                self.vista.pedir_cambio_pokemon(vivos, self.cambiar_pokemon_jugador)

                return

            # Verifica si la IA fue debilitada
            if self.ia.activo.esta_debilitado():
                if not self.ia.tiene_pokemons_vivos():
                    self.vista.agregar_log("¡Has ganado el combate!")
                    self._desactivar_botones()
                    return
                idx = self._mejor_pokemon_para_entrar()
                if idx is not None:
                    self.ia.indice_activo = idx
                    self.vista.agregar_log(f"{self.ia.activo.nombre} entra al combate.")
                    self.vista.actualizar_sprite("ia", self.ia.activo.nombre)



        self.vista.actualizar_botones(self.jugador.activo.ataques)
    
    def _mejor_pokemon_para_entrar(self):
        mejor_idx = None
        mejor_valor = float('-inf')
        atacante_jugador = self.jugador.activo

        for i, candidato in enumerate(self.ia.pokemons):
            if candidato.esta_debilitado() or i == self.ia.indice_activo:
                continue


            mejor_ataque = max((calcular_danio(candidato, atacante_jugador, atk) for atk in candidato.ataques), default=0)


            peor_recibido = max((calcular_danio(atacante_jugador, candidato, atk) for atk in atacante_jugador.ataques), default=0)


            valor = mejor_ataque - peor_recibido

            if valor > mejor_valor:
                mejor_valor = valor
                mejor_idx = i

        return mejor_idx


