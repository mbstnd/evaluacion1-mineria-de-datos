# 🧠 Evaluación 1 – Minería de Datos  
**Análisis Exploratorio, Normalización y PCA del Dataset `StudentsPerformance.csv`**

---

## 📘 Descripción del Proyecto
Este proyecto corresponde a la **primera evaluación de la asignatura Minería de Datos**, cuyo propósito es aplicar técnicas fundamentales de **análisis exploratorio de datos (EDA)**, **preprocesamiento**, **detección de outliers** y **reducción de dimensionalidad (PCA)** sobre un conjunto de datos real.

El dataset utilizado, `StudentsPerformance.csv`, recopila información sobre el rendimiento académico de **1000 estudiantes**, incluyendo variables demográficas, socioeconómicas y sus calificaciones en tres áreas principales: **Matemáticas, Lectura y Escritura**.

---

## 🎯 Objetivos del Análisis
- Explorar la estructura, calidad y tipo de variables del dataset.  
- Identificar y gestionar posibles valores faltantes.  
- Codificar variables categóricas para su análisis estadístico.  
- Aplicar **normalización Min-Max** para escalar las variables numéricas.  
- Detectar **valores atípicos (outliers)** utilizando el método del rango intercuartílico (**IQR**).  
- Clasificar a los estudiantes según su rendimiento promedio.  
- Aplicar **PCA (Análisis de Componentes Principales)** para visualizar patrones de correlación y reducir la dimensionalidad.

---

## 🧩 Librerías Utilizadas
```python
pandas
numpy
matplotlib
seaborn
scikit-learn

📊 Estructura del Dataset

Columna	Descripción
gender	Género del estudiante (male, female)
race/ethnicity	Grupo étnico o racial (group A a group E)
parental level of education	Nivel educativo de los padres
lunch	Tipo de almuerzo recibido (standard, free/reduced)
test preparation course	Curso de preparación completado (none, completed)
math score	Puntaje en Matemáticas (0–100)
reading score	Puntaje en Lectura (0–100)
writing score	Puntaje en Escritura (0–100)

⚙️ Proceso de Análisis

1️⃣ Carga y Exploración de los Datos
El dataset fue cargado utilizando Pandas, permitiendo obtener información general sobre su estructura:

Filas: 1000

Columnas: 8

Tipos de datos: 5 categóricos (object) y 3 numéricos (int64).

Valores faltantes: No se detectaron datos nulos o inconsistentes.

Este paso permitió garantizar la integridad y consistencia de los datos antes del procesamiento.

2️⃣ Transformación de Variables Categóricas

Para facilitar el análisis numérico, se codificó la variable gender mediante Label Encoding, asignando valores binarios:

female → 0

male → 1

Esta técnica es la más eficiente para variables binarias, permitiendo incluir esta variable en procesos estadísticos y en el modelo PCA.

3️⃣ Normalización (Min-Max Scaling)

Se aplicó escalamiento Min-Max a las columnas numéricas:

math score

reading score

writing score

El rango de valores fue ajustado a [0, 1], manteniendo la proporcionalidad de los datos originales.
Esta normalización permite comparar variables con distintas escalas sin distorsionar las relaciones entre ellas.

4️⃣ Detección de Valores Atípicos (IQR)

La detección de outliers se realizó utilizando el método del rango intercuartílico (IQR) y la visualización con boxplots.

Columna	Outliers detectados	Observación
math score	8	Puntajes extremadamente bajos (0–26)
reading score	6	Puntajes bajos entre 17–28
writing score	5	Puntajes bajos entre 10–23

Estos valores atípicos fueron conservados, ya que representan casos reales de bajo rendimiento académico y no errores de medición.

5️⃣ Análisis de Componentes Principales (PCA)

Se aplicó PCA sobre las variables numéricas estandarizadas:
math score, reading score, writing score, gender_encoded.

El objetivo fue reducir la dimensionalidad del conjunto de datos y detectar patrones de correlación entre variables.
El resultado mostró que los dos primeros componentes principales explican el 96.53% de la varianza total, lo cual evidencia una fuerte relación entre los puntajes académicos de las tres materias.

Además, se construyó una nueva variable categórica performance_category basada en el promedio de los tres puntajes, clasificando a los estudiantes en:

Bajo rendimiento

Rendimiento medio

Alto rendimiento

El gráfico PCA permitió visualizar estos grupos de forma clara, validando la coherencia de la clasificación.

📈 Resultados Principales

🔹 Distribución de Puntajes
Los puntajes en Matemáticas, Lectura y Escritura presentan una media cercana a 70 puntos con una desviación estándar aproximada de ±15, lo que sugiere una distribución equilibrada del rendimiento académico.

🔹 Normalización
Tras aplicar Min-Max Scaling, todos los valores quedaron dentro del rango [0, 1], facilitando su comparación y evitando sesgos por diferencias de escala.

🔹 Outliers
Los valores atípicos se concentran en los extremos inferiores de la distribución, reflejando casos reales de bajo desempeño académico, más que errores de registro.

🔹 PCA
El 96.53% de la varianza total se explica mediante los dos primeros componentes principales, confirmando la alta correlación entre las tres áreas evaluadas.
La visualización del PCA permitió identificar grupos definidos según el rendimiento general del estudiante.

🧾 Conclusión

El análisis permitió aplicar con éxito las principales etapas del preprocesamiento y exploración de datos:

Limpieza, codificación y normalización.

Identificación y justificación del tratamiento de outliers.

Aplicación efectiva de PCA para simplificar el conjunto de variables y detectar patrones globales de rendimiento.

El resultado final es un modelo interpretativo claro y visualmente representativo del desempeño académico, demostrando la aplicabilidad de las técnicas de Minería de Datos para el análisis educativo.

📂 Autor: Mario Quevedo Astudillo
💼 Carrera: Ingeniería en Informatica – Instituto Profesional San Sebastián
🗓️ Evaluación: Unidad 1 – Minería de Datos
🧰 Herramientas: Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
