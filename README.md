# 📱 Google Play Store Success Predictor: ML para la Toma de Decisiones

## 1. Motivación y Problema
En el saturado mercado de aplicaciones móviles, el **99% de las apps fallan** en alcanzar una escala comercial significativa. Para un inversionista o desarrollador, la pregunta clave es: *¿Qué atributos garantizan que una app supere el millón de descargas?*

Este proyecto nace con el objetivo de transformar datos crudos de la Play Store en un **motor de decisiones**, permitiendo predecir la probabilidad de éxito de una aplicación antes de asignar capital de desarrollo o marketing.

## 2. El Camino del Dato (Pipeline)

### 🧹 Limpieza y EDA (Análisis Exploratorio)
El dataset presentaba desafíos comunes en datos reales:
* **Tratamiento de Nulos:** Se realizó una limpieza profunda de registros incompletos (aprox. 13% de la data original).
* **Ingeniería de Variables:** Conversión de tamaños (Mbs/kbs) a una escala numérica uniforme y transformación de categorías mediante *Encoding*.
* **Insights del EDA:** Descubrimos que la mayoría de las apps exitosas son gratuitas y que el "Rating" tiene un sesgo hacia los valores altos, lo que obligó a buscar un modelo robusto que no se dejara engañar por promedios simples.

### 🏋️ Entrenamiento y Comparación de Modelos
No nos quedamos con la primera opción. Se evaluaron múltiples algoritmos para encontrar el mejor equilibrio entre sesgo y varianza:
* **Regresión Logística:** (Baseline) Buen punto de partida pero insuficiente para relaciones no lineales.
* **Árboles de Decisión:** Capturaron mejor las reglas de negocio pero con alto riesgo de *overfitting*.
* **Random Forest:** Mejoró la estabilidad.
* **XGBoost (Ganador):** Fue el modelo superior, demostrando una capacidad excepcional para manejar datos desbalanceados y relaciones complejas.

### ⚙️ Hiperparametrización y Ensamblaje
Para llevar el modelo al siguiente nivel, utilizamos **GridSearchCV**. Optimizamos parámetros críticos como:
* `n_estimators`: Para asegurar suficiente aprendizaje sin redundancia.
* `max_depth`: Controlando la complejidad del árbol.
* `learning_rate`: Ajustando la velocidad de convergencia.

**Resultado Final:** Un modelo ensamblado con un **AUC-ROC de 0.81** y un **Gini de 0.619**, superando significativamente a los modelos base.

## 3. Solución: API de Predicción
La solución final es una **API REST (Flask)** que permite consultar en tiempo real si un proyecto de App es viable.

### Lógica de Riesgo (The Investor's Threshold)
Como Ingeniero Comercial, se definió un **umbral de decisión de 0.70**. 
* Si $P(Éxito) \geq 0.70 \rightarrow$ **RECOMENDADO** (Alta convicción).
* Si $P(Éxito) < 0.70 \rightarrow$ **RECHAZADO** (Riesgo de capital no justificado).

## 4. Cómo Ejecutar la API Localmente

### Requisitos Previos
Tener Python instalado y clonar este repositorio.

### Instalación y Uso
1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt