
# Análisis Exploratorio de Datos (EDA) - Predicción de Precios de Viviendas

## 1. Importación de Librerías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar estilo de gráficos
plt.style.use("ggplot")

## 2. Cargar el Dataset
df = pd.read_csv(r"C:\Users\Usuario\OneDrive - ITESO\2.ITESO\2. Primavera 2025\Simulacion matematica\Proyecto_Optimizacion\Datos\housing_price_dataset.csv")

# Mostrar las primeras filas del dataset
df.head()

## 3. Descripción del Dataset
print("Dimensiones del dataset:", df.shape)
print("Información del dataset:")
df.info()

# Descripción estadística de las variables numéricas
df.describe()

## 4. Visualización de la Distribución de Precios
plt.figure(figsize=(10, 5))
sns.histplot(df["Price"], bins=50, kde=True)
plt.title("Distribución de Precios de Viviendas")
plt.xlabel("Precio ($)")
plt.ylabel("Frecuencia")
plt.show()

## 5. Relación entre Tamaño y Precio
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["SquareFeet"], y=df["Price"], alpha=0.5)
plt.title("Relación entre Tamaño de la Vivienda y Precio")
plt.xlabel("Tamaño en Pies Cuadrados")
plt.ylabel("Precio ($)")
plt.show()

## 6. Comparación de Precios por Vecindario
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["Neighborhood"], y=df["Price"])
plt.title("Comparación de Precios por Tipo de Vecindario")
plt.xlabel("Vecindario")
plt.ylabel("Precio ($)")
plt.show()

## 7. Correlación entre Variables Numéricas
plt.figure(figsize=(8, 6))
sns.heatmap(df.select_dtypes(include=['number']).corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de Correlación")
plt.show()
