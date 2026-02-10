# 📱 Inteligencia Artificial para la Predicción de Éxito en Google Play Store
### **Proyecto Final: Módulo 7 - Técnicas Avanzadas y Empleabilidad**
**Autor:** Alberto Güiraldes Jeria | **Bootcamp:** Ciencia de Datos e IA (UDD)

---
## 📄 Presentación del Proyecto
Puedes ver la presentación ejecutiva aquí: [Descargar PDF](./Proyecto_Final_AlbertoGuiraldes.pdf)
--

## 📊 1. Resultados Detallados del Modelo

El modelo final no solo predice, sino que discrimina con una precisión institucional. Tras el proceso de optimización, el algoritmo **XGBoost** alcanzó los siguientes niveles de confianza:

| Métrica | Valor | Significado de Negocio |
| :--- | :--- | :--- |
| **AUC-ROC** | **0.8087** | El modelo tiene un 81% de probabilidad de separar correctamente una app ganadora de una fallida. |
| **Coeficiente de Gini** | **0.6174** | Capacidad de discriminación "Fuerte", equivalente a modelos de credit scoring bancario. |
| **Average Precision (AP)** | **0.7321** | Alta fiabilidad en la captura de patrones de éxito real. |

### Matriz de Confusión y Comportamiento
El modelo se configuró bajo un enfoque **conservador**:
* **Recall Clase 0 (Fracaso): 0.79.** El modelo es excelente detectando apps que no funcionarán, protegiendo al inversionista de pérdidas de capital.
* **Precisión Clase 1 (Éxito): 0.69.** Cuando el modelo recomienda "Invertir", tiene un 69% de acierto en un mercado de altísima volatilidad.



---

## ⚙️ 2. Arquitectura Técnica: Hiperparametrización y Ensamblaje

Para este proyecto, se evitó el uso de modelos "out of the box", implementando un pipeline de optimización robusto:

### A. Tuning de Hiperparámetros (GridSearchCV)
No nos conformamos con los ajustes por defecto. Se realizó una búsqueda exhaustiva para encontrar el equilibrio entre sesgo y varianza:
* **Tasa de Aprendizaje (`learning_rate`): 0.1.** Permite una convergencia suave, evitando que el modelo ignore patrones sutiles en los Ratings.
* **Profundidad Máxima (`max_depth`): 5.** Controla la complejidad de los árboles para prevenir el *overfitting* (memorización de datos).
* **Estimadores (`n_estimators`): 100.** Cantidad óptima de árboles secuenciales para capturar la señal sin saturar el procesamiento.

### B. El Poder de los Ensambles (Voting Classifier)
Se implementó una arquitectura de **Soft Voting**, creando un "comité de expertos" que reduce el riesgo de errores individuales:
1. **XGBoost (Especialista en Sesgo):** Captura relaciones no lineales complejas entre el Precio y el Tamaño.
2. **Random Forest (Especialista en Varianza):** Aporta estabilidad y promedia las decisiones para evitar ruidos estadísticos.
3. **Logistic Regression (Base Estadística):** Proporciona una visión lineal y sobria al conjunto.



---

## 🎯 3. Análisis de Drivers: ¿Qué mueve la aguja?
Mediante el cálculo de **Importancia Relativa (F-Score Gain)**, determinamos los pilares del éxito:
1. **Precio (37.06%):** Es el filtro binario más potente. El éxito masivo es inversamente proporcional al costo inicial.
2. **Robustez Técnica - Size (28.22%):** Aplicaciones con mayor peso tienden a correlacionar con mayor éxito, sugiriendo que el mercado premia la funcionalidad completa sobre la ligereza extrema.
3. **Validación Social - Rating (21.00%):** Es un requisito de calidad mínima, pero no un driver de volumen por sí solo.



---

## 🧠 4. Conclusión Estratégica
Como Ingeniero Comercial con foco en gestión de riesgo, la conclusión del proyecto es clara: **El éxito en la Play Store es predecible, pero altamente sensible a la barrera del pago.**

El modelo demuestra que un desarrollador puede aumentar sus probabilidades de éxito en un **30% adicional** simplemente ajustando el tamaño del activo (MB) y eliminando la fricción del precio. El Coeficiente de **Gini de 0.61** valida que este sistema es una herramienta de *due diligence* robusta, capaz de filtrar proyectos de inversión tecnológica de forma cuantitativa, minimizando la exposición a Falsos Positivos y maximizando la eficiencia en la asignación de capital de marketing.



---
**Desplegado con:** Python (Flask), Scikit-Learn, XGBoost y Joblib.  
**Evaluación:** Proyecto Final Módulo 7 - UDD.


### Instalación y Uso
1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt

   