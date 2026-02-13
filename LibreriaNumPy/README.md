# Análisis de Caso: NumPy en Análisis de Datos Financieros

## 📋 Descripción

Este proyecto implementa un análisis completo del uso de NumPy para optimizar
el procesamiento de datos financieros en una empresa de análisis bursátil.

El código está organizado en una arquitectura modular que separa claramente
las responsabilidades: generación de datos, análisis, y presentación de resultados.

## 📁 Estructura del Proyecto

```
LibreriaNumPy/
│
├── main.py                    # Punto de entrada principal
│
├── src/
│   ├── __init__.py           # Convierte src en paquete Python
│   ├── datos.py              # Generación y carga de datos
│   ├── analisis.py           # Funciones de análisis y cálculo
│   └── reportes.py           # Funciones de presentación
│
├── README.md                 # Este archivo
├── informe_detallado.txt     # Documentación técnica completa
└── resumen_ejecutivo.txt     # Resumen para stakeholders
```

### Descripción de Módulos

#### `main.py` - Orquestador Principal
Coordina el flujo completo del análisis:
1. Obtención de datos
2. Procesamiento y cálculos
3. Ejecución de benchmark
4. Presentación de resultados

#### `src/datos.py` - Generación de Datos
- `generar_datos()`: Crea matriz de precios simulados
- Retorna: precios_acciones (5x5), nombres, días

#### `src/analisis.py` - Motor de Análisis
Funciones de cálculo con NumPy:
- `calcular_estadisticas()`: Promedio, máximo, mínimo
- `calcular_variaciones()`: Variación porcentual diaria
- `realizar_transformaciones()`: Logaritmos, normalización, proyecciones
- `calcular_metricas_finales()`: Métricas de portafolio

#### `src/reportes.py` - Presentación de Resultados
Funciones de formato y visualización:
- `imprimir_cabecera()`: Header del análisis
- `imprimir_matriz_precios()`: Tabla de precios
- `imprimir_estadisticas()`: Estadísticas descriptivas
- `imprimir_variaciones()`: Cambios porcentuales
- `imprimir_analisis_avanzado()`: Datos normalizados y proyecciones
- `imprimir_benchmark()`: Comparación de rendimiento
- `imprimir_resumen_ejecutivo()`: Métricas clave del portafolio

## 🚀 Instalación y Uso

### Requisitos
- Python 3.13+
- NumPy 1.20+

### Instalación
```bash
pip install numpy
```

### Ejecución
```bash
python main.py
```

## 🎯 Arquitectura y Flujo de Datos

```
main.py (Orquestador)
    │
    ├──► datos.generar_datos() → precios, nombres, dias
    │
    ├──► analisis.calcular_estadisticas() → promedios, maximos, minimos
    │
    ├──► analisis.calcular_variaciones() → variaciones
    │
    ├──► analisis.realizar_transformaciones() → rendimientos, normalizados, proyeccion
    │
    ├──► analisis.calcular_metricas_finales() → métricas de portafolio
    │
    ├──► Benchmark (NumPy vs Python)
    │
    └──► reportes.imprimir_*() → Salida formateada
```

## 📊 Resultados del Benchmark

**Test:** Cálculo de promedio en matriz 1000x1000

| Método               | Tiempo (s) | Velocidad relativa |
|---------------------|------------|-------------------|
| NumPy (vectorizado) | 0.003      | 1x (baseline)     |
| Python (bucles)     | 0.500      | 167x más lento    |

**Conclusión:** NumPy es ~150-200x más rápido que Python tradicional.

## 📖 Documentación Completa

Ver [informe_detallado.md](https://github.com/german-rs/CasosConPython/blob/main/LibreriaNumPy/informe_detallado.md) para:
- Explicación técnica de cada función
- Justificación de decisiones de diseño
- Análisis comparativo detallado
- Mejores prácticas y optimizaciones

Ver [resumen_ejecutivo.md](https://github.com/german-rs/CasosConPython/blob/main/LibreriaNumPy/resumen_ejecutivo.md) para:
- Resultados clave
- Impacto en el negocio
- Recomendaciones

---
**Elaborado por:** Germán Riveros S.
**Última actualización:** Febrero 2026  
**Versión:** 2.0 (Arquitectura Modular)