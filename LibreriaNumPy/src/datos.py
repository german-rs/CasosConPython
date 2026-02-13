import numpy as np


def generar_datos():
    np.random.seed(42)
    # Simulación de datos financieros
    precios_base = np.random.uniform(50, 150, (5, 5))
    variaciones = np.random.uniform(0.95, 1.05, (5, 5))
    precios_acciones = precios_base * variaciones

    nombres_acciones = ['TECH-A', 'BANK-B', 'ENERGY-C', 'RETAIL-D', 'PHARMA-E']
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']

    return precios_acciones, nombres_acciones, dias