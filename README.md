Markdown
# 📱 Predicción de Éxito en Google Play Store - Estrategia de Inversión con XGBoost

Este proyecto desarrolla un modelo predictivo avanzado para identificar aplicaciones móviles con alto potencial de éxito (definido como >1,000,000 de descargas). El enfoque combina rigor técnico de **Machine Learning** con una visión de **Gestión de Riesgo** financiero.

## 📈 Resumen Ejecutivo del Modelo

Tras un proceso de limpieza de datos, ingeniería de variables (EDA) y optimización de hiperparámetros mediante `GridSearchCV`, el modelo XGBoost alcanzó una capacidad predictiva sólida:

* **AUC-ROC:** 0.81
* **Coeficiente de Gini:** 0.619 (Optimizado)
* **Lógica de Inversión:** Se definió un **Escenario Conservador con un umbral de decisión del 70%**. Solo apps con una probabilidad de éxito superior a este umbral son recomendadas para inversión de capital.

## 🎯 Hallazgos Clave (Sweet Points)

A través del análisis de **Importancia de Variables** y **Gráficos de Dependencia Parcial (PDP)**, se determinaron los pilares del éxito:

1.  **Precio ($0.00):** La gratuidad es el factor de mayor peso (37.06%) para maximizar la base de usuarios inicial.
2.  **Tamaño del Archivo (~14.5 MB):** Punto de inflexión técnico; apps sobre los 20MB muestran una caída en la tasa de conversión por "fricción de descarga".
3.  **Rating (4.4+):** Umbral crítico de prueba social necesario para asegurar la viralidad orgánica.

## 🛠️ Stack Tecnológico y Estructura del Proyecto

* **Lenguaje:** Python 3.x
* **Modelo:** XGBoost (eXtreme Gradient Boosting)
* **Producción:** * `flask_app.py`: API para consumo de predicciones en tiempo real.
    * `modelo_xgboost_final.pkl`: Modelo optimizado serializado.
    * `scaler.pkl`: Escalador para asegurar la consistencia de los datos de entrada.
* **Entorno:** Desarrollado en Visual Studio Code.

## 🚀 Cómo ejecutar la API localmente

1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt