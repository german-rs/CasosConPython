import numpy as np


def calcular_estadisticas(precios_acciones):
    promedios = np.mean(precios_acciones, axis=1)
    maximos = np.max(precios_acciones, axis=1)
    minimos = np.min(precios_acciones, axis=1)
    return promedios, maximos, minimos


def calcular_variaciones(precios_acciones):
    variacion_porcentual = np.zeros((5, 4))
    for i in range(5):
        for j in range(4):
            variacion_porcentual[i, j] = ((precios_acciones[i, j + 1] - precios_acciones[i, j]) /
                                          precios_acciones[i, j]) * 100
    return variacion_porcentual


def realizar_transformaciones(precios_acciones):
    log_precios = np.log(precios_acciones)
    rendimientos_continuos = np.diff(log_precios, axis=1)

    precios_normalizados = (precios_acciones - np.mean(precios_acciones, axis=1, keepdims=True)) / \
                           np.std(precios_acciones, axis=1, keepdims=True)

    tasa_crecimiento = 0.02
    proyeccion = precios_acciones[:, -1:] * np.exp(tasa_crecimiento * np.arange(1, 6))

    return rendimientos_continuos, precios_normalizados, proyeccion


def calcular_metricas_finales(precios_acciones, variacion_porcentual):
    acciones_poseidas = 100
    valor_inicial = np.sum(precios_acciones[:, 0]) * acciones_poseidas
    valor_final = np.sum(precios_acciones[:, -1]) * acciones_poseidas
    rendimiento_portafolio = ((valor_final - valor_inicial) / valor_inicial) * 100

    volatilidad_diaria = np.std(variacion_porcentual, axis=1)
    sharpe_ratio = np.mean(variacion_porcentual, axis=1) / np.std(variacion_porcentual, axis=1)

    return valor_inicial, valor_final, rendimiento_portafolio, volatilidad_diaria, sharpe_ratio