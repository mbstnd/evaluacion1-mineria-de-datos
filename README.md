# 🧠 Evaluación 1 – Minería de Datos  
**Análisis Exploratorio, Normalización y PCA del Dataset `StudentsPerformance.csv`**

---

## 📘 Descripción del Proyecto
Este proyecto corresponde a la **primera evaluación de la asignatura Minería de Datos**, cuyo objetivo es aplicar técnicas de **análisis exploratorio, limpieza, normalización, detección de valores atípicos y reducción de dimensionalidad (PCA)** sobre un conjunto de datos real.

El dataset utilizado, `StudentsPerformance.csv`, contiene información sobre el rendimiento académico de **1000 estudiantes**, incluyendo variables demográficas, socioeconómicas y sus puntajes en tres áreas de evaluación: **Matemáticas, Lectura y Escritura**.

---

## 🎯 Objetivos del Análisis
- Explorar la estructura y calidad del dataset.  
- Identificar tipos de datos, dimensiones y posibles valores faltantes.  
- Codificar variables categóricas para su tratamiento numérico.  
- Aplicar **normalización Min-Max** para escalar los puntajes.  
- Detectar **valores atípicos** mediante el método IQR (Interquartile Range).  
- Calcular un **puntaje promedio** y clasificar a los estudiantes por rendimiento.  
- Aplicar **Análisis de Componentes Principales (PCA)** para reducir la dimensionalidad y visualizar patrones de rendimiento.

---

## 🧩 Librerías utilizadas
```python
pandas
numpy
matplotlib
seaborn
scikit-learn

## 📊 Estructura del Dataset
| Columna | Descripción |
|----------|-------------|
| gender | Género del estudiante (`male`, `female`) |
| race/ethnicity | Grupo étnico o racial (`group A` a `group E`) |
| parental level of education | Nivel educativo de los padres |
| lunch | Tipo de almuerzo recibido (`standard`, `free/reduced`) |
| test preparation course | Si completó curso de preparación (`none`, `completed`) |
| math score | Puntaje en Matemáticas (0–100) |
| reading score | Puntaje en Lectura (0–100) |
| writing score | Puntaje en Escritura (0–100) |

---

## ⚙️ Proceso de Análisis

### 1️⃣ Carga y exploración de datos  
- 1000 registros y 8 columnas.  
- Sin valores faltantes.  
- Tipos de datos correctamente definidos.

### 2️⃣ Transformación de variables categóricas  
- Se codificó la columna `gender` → `gender_encoded` (`female=0`, `male=1`).

### 3️⃣ Normalización (Min-Max Scaling)
- Columnas normalizadas: `math score`, `reading score`, `writing score`.  
- Rango resultante: `[0, 1]`.

### 4️⃣ Detección de valores atípicos (IQR)
| Columna | Outliers detectados | Comentario |
|----------|--------------------|-------------|
| math score | 8 | Puntajes muy bajos (0–26) |
| reading score | 6 | Puntajes entre 17–28 |
| writing score | 5 | Puntajes entre 10–23 |

Los valores atípicos representan casos de bajo rendimiento, no errores.

### 5️⃣ PCA (Análisis de Componentes Principales)
- Variables utilizadas: `math score`, `reading score`, `writing score`, `gender_encoded`.  
- **Varianza total explicada:** 96.53%  
- Permite visualizar con claridad los grupos de rendimiento (`Bajo`, `Medio`, `Alto`).

---

## 📈 Resultados Principales

### 🔹 Distribución de puntajes
Los tres puntajes presentan una media cercana a **70 puntos** y una desviación estándar de **±15**, reflejando un rendimiento académico balanceado.

### 🔹 Normalización
Todos los puntajes quedaron en una escala uniforme de 0 a 1, lo que facilita la comparación entre áreas.

### 🔹 Outliers
Los valores atípicos se concentran en el extremo inferior de la distribución, representando estudiantes con desempeño notablemente bajo.

### 🔹 PCA
El **96.53% de la varianza** es explicada por los dos primeros componentes principales, lo que demuestra que los puntajes de las tres materias están fuertemente correlacionados entre sí.  
El gráfico PCA permite distinguir visualmente los grupos de rendimiento académico.
