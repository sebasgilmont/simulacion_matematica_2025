# Checkpoint 1: Conjunto de Datos y Análisis Exploratorio de Datos (EDA)

## 1. Descripción del Proyecto
Este proyecto tiene como objetivo analizar y predecir los precios de viviendas utilizando un conjunto de datos de Kaggle. A través del Análisis Exploratorio de Datos (EDA), se identifican patrones y relaciones clave entre las variables, con el fin de desarrollar un modelo de optimización y predicción de precios.

## 2. Contenido del Repositorio

### **/Datos/**
- `housing_price_dataset.csv`: Conjunto de datos original con información sobre viviendas, incluyendo tamaño, número de habitaciones, baños, año de construcción, vecindario y precio.

### **/EDA/**
- `EDA.ipynb`: Notebook de Jupyter que contiene el Análisis Exploratorio de Datos (EDA), con visualizaciones y estadísticas descriptivas.

## 3. Descripción del Conjunto de Datos
El dataset contiene **50,000 registros** y las siguientes variables:

| **Variable**    | **Tipo de dato** | **Descripción** |
|---------------|--------------|----------------|
| **SquareFeet** | Entero | Tamaño de la vivienda en pies cuadrados. |
| **Bedrooms** | Entero | Número de habitaciones. |
| **Bathrooms** | Entero | Número de baños. |
| **Neighborhood** | Texto | Tipo de vecindario (Rural, Suburb, Urban). |
| **YearBuilt** | Entero | Año en que se construyó la vivienda. |
| **Price** | Decimal | Precio de la vivienda en dólares. |

No hay valores nulos en el dataset, lo que facilita el análisis.

## 4. Análisis Exploratorio de Datos (EDA)
En el archivo `EDA.ipynb`, se realizaron los siguientes análisis:
- **Descripción del dataset:** Estadísticas generales y distribución de las variables.
- **Distribución de precios:** Histogramas para visualizar la variabilidad en los precios de las viviendas.
- **Relación entre variables:** Scatterplots y boxplots para analizar la influencia del tamaño, vecindario y antigüedad en el precio.
- **Matriz de correlación:** Evaluación de la relación entre variables numéricas.

## 5. Resultados y Observaciones
- **El precio de las viviendas tiende a aumentar con el tamaño y el número de habitaciones.**
- **Las viviendas en vecindarios urbanos tienden a ser más costosas que las rurales y suburbanas.**
- **El año de construcción tiene una correlación menor con el precio, pero sigue siendo un factor relevante.**

## 6. Próximos Pasos
- Desarrollar un modelo de predicción de precios usando **Machine Learning**.
- Evaluar diferentes algoritmos para mejorar la precisión del modelo.
- Implementar un sistema de optimización para recomendar precios competitivos.

## 7. Autores y Créditos
Este proyecto fue desarrollado como parte del curso de **Simulación Matemática**, utilizando un dataset público de Kaggle.

**Contacto:** Para dudas o colaboraciones, por favor, contactar a los integrantes del equipo.

---

**Nota:** Si es necesario, este README puede ser actualizado conforme avance el proyecto.
