# modelo/ataque.py

class Ataque:
    def __init__(self, nombre, tipo, categoria, poder):
        self.nombre = nombre
        self.tipo = tipo.lower()
        self.categoria = categoria.lower()  # "fisico" o "especial"
        self.poder = poder

    def es_danio(self):
        return True
