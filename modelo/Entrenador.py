# modelo/entrenador.py

class Entrenador:
    def __init__(self, pokemons):
        self.pokemons = pokemons
        self.indice_activo = 0

    @property
    def activo(self):
        return self.pokemons[self.indice_activo]

    def cambiar_pokemon(self):
        for i, p in enumerate(self.pokemons):
            if not p.esta_debilitado():
                self.indice_activo = i
                print(f"{self.activo.nombre} entra al combate!")
                return True
        return False

    def tiene_pokemons_vivos(self):
        return any(not p.esta_debilitado() for p in self.pokemons)
