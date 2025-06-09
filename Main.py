import tkinter as tk
from modelo.pokemon import Pokemon
from modelo.Ataque import Ataque
from modelo.Entrenador import Entrenador
from modelo.Combate import Combate
from vista.vista import PantallaSeleccionEquipos, PantallaSeleccionMovimientos, Vista
from controlador.controlador import Controlador

def convertir_dict_a_pokemon(data_dict):
    return Pokemon(
        nombre=data_dict["nombre"],
        nivel=30,
        ps=int(data_dict["ps"]),
        ataque_fisico=int(data_dict["ataque"]),
        defensa_fisica=int(data_dict["defensa"]),
        ataque_especial=int(data_dict["ataque_especial"]),
        defensa_especial=int(data_dict["defensa_especial"]),
        velocidad=int(data_dict["velocidad"]),
        tipo1=data_dict["tipo1"].lower(),
        tipo2=data_dict["tipo2"].lower() if data_dict["tipo2"] else None
    )

def iniciar_app():
    root = tk.Tk()
    PantallaSeleccionEquipos(root, "utils/pokedex.csv", lambda eq_j, eq_ia: seleccionar_movs(root, eq_j, eq_ia))
    root.mainloop()


def seleccionar_movs(root, equipo_jugador, equipo_ia):
    for widget in root.winfo_children():
        widget.destroy()
    PantallaSeleccionMovimientos(root, equipo_jugador, lambda eq_final: seleccionar_movs_ia(root, eq_final, equipo_ia))

def seleccionar_movs_ia(root, equipo_jugador_listo, equipo_ia):
    for widget in root.winfo_children():
        widget.destroy()
    PantallaSeleccionMovimientos(root, equipo_ia, lambda eq_ia_final: iniciar_combate(root, equipo_jugador_listo, eq_ia_final))

def iniciar_combate(root, pokemons_jugador_dict, pokemons_ia_dict):
    for widget in root.winfo_children():
        widget.destroy()
    
    jugador_objs = [convertir_dict_a_pokemon(p) for p in pokemons_jugador_dict]
    ia_objs = [convertir_dict_a_pokemon(p) for p in pokemons_ia_dict]

    for i, p in enumerate(jugador_objs):
        p.ataques = pokemons_jugador_dict[i]["ataques"]
    for i, p in enumerate(ia_objs):
        p.ataques = pokemons_ia_dict[i]["ataques"]

    jugador = Entrenador(jugador_objs)
    ia = Entrenador(ia_objs)
    combate = Combate(jugador, ia)

    vista = Vista(root, "assets/background.png", None)
    Controlador(jugador, ia, vista, combate)


if __name__ == "__main__":
    root = tk.Tk()
    PantallaSeleccionEquipos(root, "pokedex.csv", lambda eq_j, eq_ia: seleccionar_movs(root, eq_j, eq_ia))
    root.mainloop()

