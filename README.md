# Trabajo Integrador Final – Modelos y Simulación

**Grupo 3**

## Descripción

Este repositorio contiene el desarrollo del Trabajo Integrador Final de la asignatura **Modelos y Simulación**.

El proyecto consiste en la implementación y simulación de modelos de producción, considerando diferentes condiciones de operación. Se busca analizar los resultados obtenidos mediante simulaciones computacionales y compararlos con los resultados presentados en el artículo científico de referencia.

## Estructura del repositorio

```text
TIF_MyS_G3/
│
├── articulo/
│   ├── Discrete_E...ng_Systems.pdf
│
├── notebooks/
│   └── TFI_MyS.ipynb
|
├── scr/
|    └── modelo1.py
|    └── modelo2.py
|    └── modelo3.py
|    └── parametros.py
|
├── informe/
│   └── TFI_MyS_G3.ipynb
├── requirements.txt
├── referencias.md
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

