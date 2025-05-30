# modelo/pokemon.py

class Pokemon:
    def __init__(self, nombre, nivel, ps, ataque_fisico, defensa_fisica, ataque_especial, defensa_especial, velocidad, tipo1, tipo2=None):
        self.nombre = nombre
        self.nivel = nivel
        self.ps_max = ps
        self.ps_actual = ps
        self.tipo1 = tipo1.lower()
        self.tipo2 = tipo2.lower() if tipo2 else None
        self.ataques = []

        self.base_stats = {
            "ataque": ataque_fisico,
            "defensa": defensa_fisica,
            "ataque especial": ataque_especial,
            "defensa especial": defensa_especial,
            "velocidad": velocidad
        }

    def get_estadistica(self, estadistica):
        return self.base_stats.get(estadistica.lower(), 0)

    def recibir_daño(self, cantidad):
        self.ps_actual = max(0, self.ps_actual - cantidad)

    def esta_debilitado(self):
        return self.ps_actual <= 0
