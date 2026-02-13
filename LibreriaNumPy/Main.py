from src.datos import generar_datos
from src.analisis import (calcular_estadisticas, calcular_variaciones,
                          realizar_transformaciones, calcular_metricas_finales)
from src.reportes import *  # Importamos todas las funciones de reporte
import time
import numpy as np


def main():
    # 1. OBTENCIÓN DE DATOS
    precios, nombres, dias = generar_datos()

    # 2. PROCESAMIENTO (CÁLCULOS)
    promedios, maximos, minimos = calcular_estadisticas(precios)
    variaciones = calcular_variaciones(precios)
    rendimientos, normalizados, proyeccion = realizar_transformaciones(precios)
    v_ini, v_fin, rend_port, vol, sharpe = calcular_metricas_finales(precios, variaciones)

    # 3. EJECUCIÓN DEL BENCHMARK (Necesario para los tiempos)
    datos_g = np.random.uniform(50, 150, (1000, 1000))
    t_ini = time.time()
    _ = np.mean(datos_g, axis=1)
    t_numpy = time.time() - t_ini

    t_ini = time.time()
    for fila in datos_g:
        _ = sum(fila) / len(fila)
    t_python = time.time() - t_ini

    # 4. PRESENTACIÓN DE RESULTADOS (REPORTES)
    imprimir_cabecera()
    imprimir_matriz_precios(nombres, dias, precios)
    imprimir_estadisticas(nombres, promedios, maximos, minimos)
    imprimir_variaciones(nombres, variaciones)
    imprimir_analisis_avanzado(nombres, dias, normalizados, proyeccion, precios)
    imprimir_benchmark(t_numpy, t_python)
    imprimir_resumen_ejecutivo(v_ini, v_fin, rend_port, sharpe, nombres)

    print("\n" + "=" * 80)
    print("FIN DEL ANÁLISIS")
    print("=" * 80)


if __name__ == "__main__":
    main()