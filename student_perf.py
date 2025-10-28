# 1️⃣ Importación de librerías principales
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# 2️⃣ Cargar y exploracion de los datos
df = pd.read_csv(r'c:/workspace/01-mineria-de-datos/StudentsPerformance.csv')
print("\n 📏 Dimensiones del dataset:", df.shape)
print("\n 📊 Tipos de datos por columna:\n", df.dtypes)
print("\n 🧾 Primeras filas del dataset:\n", df.head())

# 3️⃣ Detección de valores faltantes

missing_values = df.isnull().sum()
print('\n Valores faltantes por columna:\n', missing_values)

###
# Tras aplicar df.isnull().sum(), se observa que no existen valores faltantes
# en ninguna columna del dataset.
# Esto significa que no es necesario realizar imputaciones ni eliminar registros.
###
# 4️⃣ Transformacion de datos categóricos ( female = 0, male = 1 )

# Verificar la columna de género 'y su distribución
print("\n 🔍 Análisis de la columna 'gender' (género):")
print(f"  Valores únicos: {df['gender'].unique()}")

df['gender_encoded'] = df['gender'].map({'female': 0, 'male': 1})



# Mostrar el mapeo realizado
print("\n✅ Transformación aplicada:")
print(f"  {df['gender'].unique()[0]} → {df['gender_encoded'].unique()[0]}")
print(f"  {df['gender'].unique()[1]} → {df['gender_encoded'].unique()[1]}")

# Verificar el resultado
print("\n📊 Comparación antes y después:")
comparison = pd.DataFrame({
      'gender_original': df['gender'].head(10),
      'gender_encoded': df['gender_encoded'].head(10)
  })
print(comparison)


# 5️⃣ Normalización de datos con Min-Max Scaling

# Columnas de puntajes a normalizar
score_columns = ['math score', 'reading score', 'writing score']
print("\n 📊 Análisis ANTES de la normalización:")
print("="*60)
for col in score_columns:
     print(f"\n{col}:")
     print(f"  Rango original: [{df[col].min()}, {df[col].max()}]")
     print(f"  Media: {df[col].mean():.2f}")
     print(f"  Desviación estándar: {df[col].std():.2f}")

# Mostrar primeras filas originales
print("\n🔍 Primeras 5 filas - Valores originales:")
print(df[score_columns].head(5))

# Aplicar Min-Max Scaling
scaler = MinMaxScaler()
df_normalized = df.copy()
df_normalized[score_columns] = scaler.fit_transform(df[score_columns])

# Mostrar datos post min max scaling
range_after = df_normalized[score_columns].agg(['min', 'max']).T
print("\n" + "="*60)
print("✅ Normalización aplicada con Min-Max Scaling")
print("="*60)

print("\n📊 Rango de valores tras Min-Max Scaling:")
for col in score_columns:
    print(f"  {col}: min = {df_normalized[col].min():.2f}, max = {df_normalized[col].max():.2f}")


# 6️⃣ Detección de valores atípicos
print("\n🔍 Detección de valores atípicos:")
print("=" * 60)

plt.figure(figsize=(10, 6))
sns.boxplot(data=df[score_columns], palette="Set3")
plt.title('Boxplot de Puntajes de Estudiantes')
plt.ylabel('Puntaje')
plt.xlabel('Período')
plt.grid(True, alpha=0.3)
plt.show()

# Identificación de outliers usando el método del IQR

print("\n📈 Identificación de outliers mediante el método del IQR:")
print("=" * 60)

def detected_outliers_iqr(series):
    """
    Detecta valores atípicos (outliers) en una serie numérica usando el método del IQR.
    Parámetros:
        series (pd.Series): columna numérica del DataFrame
    Retorna:
        outliers (pd.Series): valores considerados como atípicos
    """
    # Calcular cuartiles
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1

    # Calcular límites
    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    # Filtrar los valores fuera del rango
    outliers = series[(series < lower_limit) | (series > upper_limit)]

    print(f"📊 Columna analizada: {series}")
    print(f" - Q1 (25%): {Q1:.2f}")
    print(f" - Q3 (75%): {Q3:.2f}")
    print(f" - IQR: {IQR:.2f}")
    print(f" - Límite inferior: {lower_limit:.2f}")
    print(f" - Límite superior: {upper_limit:.2f}")
    print(f" - Cantidad de outliers: {len(outliers)}\n")

    return outliers

for col in score_columns:
    outliers = detected_outliers_iqr(df[col])
    if not outliers.empty:
        print(f"🔸 Outliers encontrados en {col}: {list(outliers.values)}\n")
    else:
        print(f"✅ No se detectaron outliers en {col}.\n")



# 7️⃣ Análisis de componentes principales (PCA)
print("\n🔍 Análisis de Componentes Principales (PCA):")
print("=" * 60)

# Selección de características numéricas
numeric_features = df.select_dtypes(include=[np.number]).columns.tolist()
print(f"🔸 Características numéricas seleccionadas para PCA: {numeric_features}")

# Estandarización de los datos
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[numeric_features])

# Aplicación de PCA con 2 componentes
pca = PCA(n_components=2)
pca_result = pca.fit_transform(df_scaled)

# Resultados del PCA
print("\n✅ PCA aplicado con éxito.")
print(f"🔸 Varianza explicada por cada componente: {pca.explained_variance_ratio_}")
print(f"🔹 Varianza total explicada: {np.sum(pca.explained_variance_ratio_) * 100:.2f}%")

# Crear categorías basadas en el promedio de las tres calificaciones
df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
df['performance_category'] = pd.qcut(df['average_score'], q=3, labels=['Bajo', 'Medio', 'Alto'])

# DataFrame con resultados y categoría
pca_df = pd.DataFrame(pca_result, columns=['PCA1', 'PCA2'])
pca_df['Rendimiento'] = df['performance_category']

# Visualización de los resultados
plt.figure(figsize=(10, 6))
sns.scatterplot(x='PCA1', y='PCA2', data=pca_df, hue='Rendimiento', palette="Set2")
plt.title('PCA de Características Numéricas por Nivel de Rendimiento')
plt.xlabel('Primer Componente Principal')
plt.ylabel('Segundo Componente Principal')
plt.grid(True, alpha=0.3)
plt.legend(title='Nivel de Rendimiento')
plt.show()