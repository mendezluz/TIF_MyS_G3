# Trabajo Integrador Final – Modelos y Simulación

**Grupo 3**

## Descripción

Este repositorio contiene el desarrollo del Trabajo Integrador Final de la asignatura **Modelos y Simulación**.

El proyecto consiste en la implementación y simulación de modelos de producción, considerando diferentes condiciones de operación. Se busca analizar los resultados obtenidos mediante simulaciones computacionales y compararlos con los resultados presentados en el artículo científico de referencia.

## Estructura del repositorio

```text
TIF_MyS_G3/
│
├── documentos/
│   ├── documento1.pdf
│   └── documento2.pdf
│
├── notebooks/
│   └── implementacion_robots.ipynb
│
├── modelo2.py
├── parametros.py
├── requirements.txt
│
└── README.md
```

## Tecnologías utilizadas

- Python
- NumPy
- Pandas
- Matplotlib
- Google Colab

## Instalación y ejecución

Las simulaciones se ejecutan mediante notebooks de Google Colab.

1. Ingresar al repositorio y abrir el notebook correspondiente.
2. Seleccionar la opción **Open in Colab**.
3. Ejecutar las celdas en orden.

El notebook descarga el repositorio de GitHub e instala las dependencias especificadas en `requirements.txt`.

```python
!pip install -r /content/TIF_MyS_G3/requirements.txt
```

## Implementación

La implementación se encuentra organizada en los siguientes archivos:

- **`modelo2.py`**: contiene la función de simulación del modelo de robots.
- **`parametros.py`**: contiene los parámetros utilizados por los modelos.
- **`notebooks/`**: contiene los experimentos, las ejecuciones de las simulaciones y el análisis de resultados.

## Resultados

Se realizan múltiples ejecuciones para distintos horizontes temporales. A partir de ellas se calculan indicadores como:

- Producción promedio.
- Desviación estándar.
- Desviación relativa.
- Eficiencia global de los equipos (OEE).

Los resultados obtenidos se comparan con los valores informados en el artículo científico de referencia.

## Reproducibilidad

Se establece una semilla aleatoria para facilitar la reproducción de los experimentos. Además, las dependencias necesarias se encuentran especificadas en `requirements.txt`.

Para reproducir los resultados se debe ejecutar el notebook desde el comienzo, respetando el orden de las celdas.

