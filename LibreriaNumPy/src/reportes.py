import time
import numpy as np

def imprimir_cabecera():
    print("=" * 80)
    print("ANÁLISIS FINANCIERO CON NUMPY - Caso de Estudio")
    print("=" * 80)

def imprimir_matriz_precios(nombres, dias, precios):
    print("\n📊 MATRIZ DE PRECIOS DE ACCIONES (5 acciones x 5 días)")
    print("-" * 80)
    print(f"{'Acción':<12}", end="")
    for dia in dias:
        print(f"{dia:>12}", end="")
    print("\n" + "-" * 80)
    for i, nombre in enumerate(nombres):
        print(f"{nombre:<12}", end="")
        for j in range(5):
            print(f"${precios[i, j]:>10.2f}", end=" ")
        print()

def imprimir_estadisticas(nombres, promedios, maximos, minimos):
    print("\n" + "=" * 80)
    print("ANÁLISIS ESTADÍSTICO")
    print("=" * 80)
    print("\n📈 ESTADÍSTICAS POR ACCIÓN")
    print("-" * 80)
    print(f"{'Acción':<12} {'Promedio':>12} {'Máximo':>12} {'Mínimo':>12} {'Rango':>12}")
    print("-" * 80)
    for i, nombre in enumerate(nombres):
        rango = maximos[i] - minimos[i]
        print(f"{nombre:<12} ${promedios[i]:>10.2f} ${maximos[i]:>10.2f} ${minimos[i]:>10.2f} ${rango:>10.2f}")

def imprimir_variaciones(nombres, variacion_porcentual):
    print("\n📊 VARIACIÓN PORCENTUAL DIARIA (%)")
    print("-" * 80)
    print(f"{'Acción':<12} {'Lun→Mar':>12} {'Mar→Mié':>12} {'Mié→Jue':>12} {'Jue→Vie':>12} {'Promedio':>12}")
    print("-" * 80)
    for i, nombre in enumerate(nombres):
        print(f"{nombre:<12}", end="")
        for j in range(4):
            print(f"{variacion_porcentual[i, j]:>11.2f}%", end=" ")
        print(f"{np.mean(variacion_porcentual[i]):>11.2f}%")

def imprimir_analisis_avanzado(nombres, dias, normalizados, proyeccion, precios_originales):
    print("\n📏 DATOS NORMALIZADOS (Z-Score)")
    print("-" * 80)
    print(f"{'Acción':<12}", end="")
    for dia in dias:
        print(f"{dia:>12}", end="")
    print("\n" + "-" * 80)
    for i, nombre in enumerate(nombres):
        print(f"{nombre:<12}", end="")
        for j in range(5):
            print(f"{normalizados[i, j]:>12.3f}", end="")
        print()

    print(f"\n📈 PROYECCIÓN DE PRECIOS (Crecimiento 2.0% diario)")
    print("-" * 80)
    for i, nombre in enumerate(nombres):
        print(f"{nombre}: Precio actual ${precios_originales[i, -1]:.2f} → Proyección 5 días ${proyeccion[i, -1]:.2f}")

def imprimir_benchmark(tiempo_numpy, tiempo_python):
    print("\n" + "=" * 80)
    print("COMPARACIÓN: NUMPY vs. PYTHON TRADICIONAL")
    print("=" * 80)
    print(f"\n⏱️  BENCHMARK: Cálculo de estadísticas en matriz 1000x1000")
    print("-" * 80)
    print(f"{'Método':<20} {'Tiempo (s)':>15} {'Velocidad relativa':>20}")
    print("-" * 80)
    print(f"{'NumPy (vectorizado)':<20} {tiempo_numpy:>15.6f} {'1x (baseline)':>20}")
    print(f"{'Python (bucles)':<20} {tiempo_python:>15.6f} {f'{tiempo_python/tiempo_numpy:.1f}x más lento':>20}")

def imprimir_resumen_ejecutivo(v_inicial, v_final, rendimiento, sharpe, nombres):
    print("\n" + "=" * 80)
    print("RESUMEN EJECUTIVO")
    print("=" * 80)
    print(f"Valor inicial: ${v_inicial:,.2f} | Valor final: ${v_final:,.2f}")
    print(f"Rendimiento semanal: {rendimiento:.2f}%")
    print(f"\n⭐ RATIO DE SHARPE POR ACCIÓN:")
    for i, nombre in enumerate(nombres):
        print(f"    {nombre}: {sharpe[i]:.3f}")