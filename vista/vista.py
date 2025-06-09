# vista/interfaz.py

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import csv

from utils.filtro import filtrar_movimientos
from utils.movesets import ATAQUES_DISPONIBLES

# ------------------------------------------------------
# 🧩 Clase 1: PantallaSeleccionEquipos
# ------------------------------------------------------

class PantallaSeleccionEquipos:
    def __init__(self, root, pokedex_path, on_finalizar):
        self.root = root
        self.root.title("Configuración de Equipos")
        self.pokedex_path = pokedex_path
        self.on_finalizar = on_finalizar

        self.pokedex = self.cargar_pokedex()
        self.pokedex.sort(key=lambda p: int(p["id"]))  # orden por número
        self.nombres = [p["nombre"] for p in self.pokedex]


        self.selecciones = {"jugador": [], "ia": []}
        self.interfaz_seleccion_equipos()

    def cargar_pokedex(self):
        ruta_absoluta = os.path.join(os.path.dirname(__file__), '..', 'utils', self.pokedex_path)
        ruta_absoluta = os.path.abspath(ruta_absoluta)
        with open(ruta_absoluta, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader]

    def interfaz_seleccion_equipos(self):
        tk.Label(self.root, text="Tu Equipo", font=("Arial", 14)).pack(pady=5)
        frame_jugador = tk.Frame(self.root)
        frame_jugador.pack(pady=5)
        self.boxes_jugador = self.crear_fila_seleccion(frame_jugador, "jugador")

        tk.Label(self.root, text="Equipo IA", font=("Arial", 14)).pack(pady=5)
        frame_ia = tk.Frame(self.root)
        frame_ia.pack(pady=5)
        self.boxes_ia = self.crear_fila_seleccion(frame_ia, "ia")

        self.boton_ok = tk.Button(self.root, text="OK", command=self.confirmar_seleccion)
        self.boton_ok.pack(pady=15)

    def crear_fila_seleccion(self, parent, quien):
        boxes = []
        for i in range(3):
            cb = ttk.Combobox(parent, values=self.nombres, state="readonly", width=15)
            cb.grid(row=0, column=i, padx=5)
            cb.bind("<<ComboboxSelected>>", lambda e: self.actualizar_opciones())
            boxes.append(cb)
        self.selecciones[quien] = boxes
        return boxes

    def actualizar_opciones(self):
        for quien, boxes in [("jugador", self.boxes_jugador), ("ia", self.boxes_ia)]:
            seleccionados = set(box.get() for box in boxes if box.get())
            disponibles = [p["nombre"] for p in self.pokedex if p["nombre"] not in seleccionados]

            for box in boxes:
                actual = box.get()
                valores = [p["nombre"] for p in self.pokedex if p["nombre"] == actual or p["nombre"] in disponibles]
                box["values"] = valores



    def confirmar_seleccion(self):
        nombres_jugador = [box.get() for box in self.boxes_jugador]
        nombres_ia = [box.get() for box in self.boxes_ia]

        if "" in nombres_jugador or "" in nombres_ia:
            messagebox.showerror("Error", "Todos los combobox deben estar seleccionados.")
            return

        equipo_jugador = [p for p in self.pokedex if p["nombre"] in nombres_jugador]
        equipo_ia = [p for p in self.pokedex if p["nombre"] in nombres_ia]
        self.on_finalizar(equipo_jugador, equipo_ia)


class PantallaSeleccionMovimientos:
    def __init__(self, root, pokemones, on_finalizar):
        self.root = root
        self.root.title("Seleccionar Ataques")
        self.pokemones = pokemones
        self.on_finalizar = on_finalizar
        self.frames = []

        self.crear_interfaz()
        self.boton_ok = tk.Button(root, text="Confirmar movimientos", command=self.confirmar)
        self.boton_ok.pack(pady=10)

    def crear_interfaz(self):
        for p in self.pokemones:
            frame = tk.LabelFrame(self.root, text=p["nombre"])
            frame.pack(padx=10, pady=5)
            boxes = []

            stats = {
                "ataque": int(p["ataque"]),
                "ataque_especial": int(p["ataque_especial"])
            }

            poke_obj = type("PokemonTemp", (), {
                "nombre": p["nombre"],
                "tipo1": p["tipo1"].lower(),
                "tipo2": p["tipo2"].lower() if p["tipo2"] else None,
                "get_estadistica": lambda self, stat: stats.get(stat.lower(), 0)
            })()

            ataques_validos = filtrar_movimientos(poke_obj, ATAQUES_DISPONIBLES)
            nombres_validos = sorted([a.nombre for a in ataques_validos])

            for _ in range(4):
                cb = ttk.Combobox(frame, values=nombres_validos, state="readonly", width=20)
                cb.pack(side="left", padx=5)
                boxes.append(cb)

            self.frames.append((p, boxes))

    def confirmar(self):
        for p, boxes in self.frames:
            nombres = [cb.get() for cb in boxes]
            if len(set(nombres)) < 4:
                messagebox.showerror("Error", f"{p['nombre']} tiene ataques repetidos")
                return
            ataques = [a for a in ATAQUES_DISPONIBLES if a.nombre in nombres]
            p["ataques"] = ataques

        self.on_finalizar(self.pokemones)

class Vista:
    def __init__(self, root, fondo_path, on_ataque):
        self.root = root
        self.root.title("Pokeminmax - Combate")
        self.on_ataque = on_ataque
        self.imagenes = {"jugador": None, "ia": None}

        fondo = Image.open(fondo_path)
        self.fondo_img = ImageTk.PhotoImage(fondo)
        self.canvas = tk.Canvas(root, width=fondo.width, height=fondo.height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor="nw", image=self.fondo_img)

        self.sprites = {
            "jugador": self.canvas.create_image(180, 330, anchor="center"),
            "ia": self.canvas.create_image(630, 110, anchor="center")
        }

        self.log = tk.Text(root, height=8, width=60, bg="black", fg="lime", state="disabled")
        self.log.pack(pady=5)

        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack()
        self.botones = []
        for i in range(4):
            btn = tk.Button(self.frame_botones, text=f"Ataque {i+1}", width=15,
                            command=lambda idx=i: self.on_ataque(idx))
            btn.grid(row=0, column=i, padx=5)
            self.botones.append(btn)

        self.redirigir_print()

    def actualizar_botones(self, ataques):
        for i in range(4):
            if i < len(ataques):
                self.botones[i]["text"] = ataques[i].nombre
                self.botones[i]["state"] = "normal"
            else:
                self.botones[i]["text"] = "-"
                self.botones[i]["state"] = "disabled"

    def agregar_log(self, texto):
        self.log["state"] = "normal"
        self.log.insert("end", texto + "\n")
        self.log["state"] = "disabled"
        self.log.see("end")

    def pedir_cambio_pokemon(self, opciones, callback):
        ventana = tk.Toplevel(self.root)
        ventana.title("Elige tu siguiente Pokémon")
        tk.Label(ventana, text="Tu Pokémon se debilitó. Elige otro:").pack(pady=10)
        for i, p in enumerate(opciones):
            btn = tk.Button(ventana, text=p.nombre, width=20, command=lambda idx=i: [callback(idx), ventana.destroy()])
            btn.pack(pady=2)

    def actualizar_sprite(self, quien, nombre_pokemon):
        ruta = f"assets/Pokemon/{nombre_pokemon}.png"
        if not os.path.exists(ruta):
            print(f"Imagen no encontrada: {ruta}")
            return
        imagen = Image.open(ruta).resize((80, 80))
        tk_imagen = ImageTk.PhotoImage(imagen)
        self.imagenes[quien] = tk_imagen
        self.canvas.itemconfig(self.sprites[quien], image=tk_imagen)

    def desactivar_botones_ataque(self):
        for b in self.botones:
            b["state"] = "disabled"

    def activar_botones_ataque(self):
        for b in self.botones:
            b["state"] = "normal"

    def redirigir_print(self):
        import sys
        class Redirigir:
            def __init__(self, escribir):
                self.escribir = escribir
            def write(self, mensaje):
                if mensaje.strip():
                    self.escribir(mensaje.strip())
            def flush(self): pass
        sys.stdout = Redirigir(self.agregar_log)
        sys.stderr = Redirigir(self.agregar_log)
