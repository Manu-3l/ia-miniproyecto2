# utils/efectividades.py

EFECTIVIDADES = {

    # NORMAL
    ('normal', 'roca'): 0.5, ('normal', 'fantasma'): 0.0, ('normal', 'acero'): 0.5,

    # FUEGO
    ('fuego', 'fuego'): 0.5, ('fuego', 'agua'): 0.5, ('fuego', 'planta'): 2.0,
    ('fuego', 'hielo'): 2.0, ('fuego', 'bicho'): 2.0, ('fuego', 'roca'): 0.5,
    ('fuego', 'dragón'): 0.5, ('fuego', 'acero'): 2.0,

    # AGUA
    ('agua', 'fuego'): 2.0, ('agua', 'agua'): 0.5, ('agua', 'planta'): 0.5,
    ('agua', 'tierra'): 2.0, ('agua', 'roca'): 2.0, ('agua', 'dragón'): 0.5,

    # ELÉCTRICO
    ('eléctrico', 'agua'): 2.0, ('eléctrico', 'eléctrico'): 0.5,
    ('eléctrico', 'planta'): 0.5, ('eléctrico', 'tierra'): 0.0,
    ('eléctrico', 'volador'): 2.0, ('eléctrico', 'dragón'): 0.5,

    # PLANTA
    ('planta', 'fuego'): 0.5, ('planta', 'agua'): 2.0, ('planta', 'planta'): 0.5,
    ('planta', 'veneno'): 0.5, ('planta', 'tierra'): 2.0, ('planta', 'volador'): 0.5,
    ('planta', 'bicho'): 0.5, ('planta', 'roca'): 2.0, ('planta', 'dragón'): 0.5,
    ('planta', 'acero'): 0.5,

    # HIELO
    ('hielo', 'fuego'): 0.5, ('hielo', 'agua'): 0.5, ('hielo', 'planta'): 2.0,
    ('hielo', 'tierra'): 2.0, ('hielo', 'volador'): 2.0, ('hielo', 'dragón'): 2.0,
    ('hielo', 'acero'): 0.5,

    # LUCHA
    ('lucha', 'normal'): 2.0, ('lucha', 'hielo'): 2.0, ('lucha', 'veneno'): 0.5,
    ('lucha', 'volador'): 0.5, ('lucha', 'psíquico'): 0.5, ('lucha', 'bicho'): 0.5,
    ('lucha', 'roca'): 2.0, ('lucha', 'fantasma'): 0.0, ('lucha', 'siniestro'): 2.0,
    ('lucha', 'acero'): 2.0, ('lucha', 'hada'): 0.5,

    # VENENO
    ('veneno', 'planta'): 2.0, ('veneno', 'veneno'): 0.5, ('veneno', 'tierra'): 0.5,
    ('veneno', 'roca'): 0.5, ('veneno', 'fantasma'): 0.5, ('veneno', 'acero'): 0.0,
    ('veneno', 'hada'): 2.0,

    # TIERRA
    ('tierra', 'fuego'): 2.0, ('tierra', 'eléctrico'): 2.0, ('tierra', 'planta'): 0.5,
    ('tierra', 'veneno'): 2.0, ('tierra', 'volador'): 0.0, ('tierra', 'roca'): 2.0,
    ('tierra', 'acero'): 2.0,

    # VOLADOR
    ('volador', 'eléctrico'): 0.5, ('volador', 'planta'): 2.0, ('volador', 'lucha'): 2.0,
    ('volador', 'bicho'): 2.0, ('volador', 'roca'): 0.5, ('volador', 'acero'): 0.5,

    # PSÍQUICO
    ('psíquico', 'lucha'): 2.0, ('psíquico', 'veneno'): 2.0, ('psíquico', 'psíquico'): 0.5,
    ('psíquico', 'acero'): 0.5, ('psíquico', 'siniestro'): 0.0,

    # BICHO
    ('bicho', 'fuego'): 0.5, ('bicho', 'planta'): 2.0, ('bicho', 'lucha'): 0.5,
    ('bicho', 'veneno'): 0.5, ('bicho', 'volador'): 0.5, ('bicho', 'psíquico'): 2.0,
    ('bicho', 'fantasma'): 0.5, ('bicho', 'siniestro'): 2.0, ('bicho', 'acero'): 0.5,
    ('bicho', 'hada'): 0.5,

    # ROCA
    ('roca', 'fuego'): 2.0, ('roca', 'hielo'): 2.0, ('roca', 'lucha'): 0.5,
    ('roca', 'tierra'): 0.5, ('roca', 'volador'): 2.0, ('roca', 'bicho'): 2.0,
    ('roca', 'acero'): 0.5,

    # FANTASMA
    ('fantasma', 'normal'): 0.0, ('fantasma', 'psíquico'): 2.0, ('fantasma', 'fantasma'): 2.0,
    ('fantasma', 'siniestro'): 0.5,

    # DRAGÓN
    ('dragón', 'dragón'): 2.0, ('dragón', 'acero'): 0.5, ('dragón', 'hada'): 0.0,

    # SINIESTRO
    ('siniestro', 'lucha'): 0.5, ('siniestro', 'psíquico'): 2.0,
    ('siniestro', 'fantasma'): 2.0, ('siniestro', 'siniestro'): 0.5,
    ('siniestro', 'hada'): 0.5,

    # ACERO
    ('acero', 'fuego'): 0.5, ('acero', 'agua'): 0.5, ('acero', 'eléctrico'): 0.5,
    ('acero', 'hielo'): 2.0, ('acero', 'roca'): 2.0, ('acero', 'hada'): 2.0,

    # HADA
    ('hada', 'fuego'): 0.5, ('hada', 'lucha'): 2.0, ('hada', 'veneno'): 0.5,
    ('hada', 'dragón'): 2.0, ('hada', 'siniestro'): 2.0, ('hada', 'acero'): 0.5


}
