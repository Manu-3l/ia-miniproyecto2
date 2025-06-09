MOVIMIENTOS_PERMITIDOS_POR_TIPO = {
    "fuego": ["fuego", "normal", "lucha"],
    "agua": ["agua", "hielo", "normal"],
    "planta": ["planta", "normal", "veneno"],
    "electrico": ["electrico", "normal", "acero"],
    "lucha": ["lucha", "normal"],
    "normal": ["normal", "fuego", "planta","agua","electrico",  "acero", "tierra", "roca", "lucha"],
    "roca": ["roca", "normal", "tierra"],
    "fantasma": ["fantasma", "siniestro"],
    "veneno": ["veneno", "bicho", "normal"],
    "acero": ["acero", "normal", "lucha"],
    "hielo": ["hielo", "normal"],
    "volador": ["volador","normal"],
    "hada": ["psiquico", "normal","hada"],
    "psiquico": ["normal", "fuego", "planta","agua","electrico","psiquico"],
    "dragon": ["agua", "fuego", "dragon","agua","electrico"],
    "tierra": ["tierra", "roca", "lucha"],
    "bicho": ["bicho", "normal", "veneno"]

}
