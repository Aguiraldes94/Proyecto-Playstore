from flask import Flask, request, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__)

# 1. CONFIGURACIÓN DE RUTAS Y CARGA DEL MODELO
# Usamos BASE_DIR para que la API encuentre el archivo .pkl sin importar desde dónde la ejecutes
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Asegúrate de que el nombre del archivo sea exactamente este en tu carpeta:
NOMBRE_MODELO = "modelo_xgboost_final.pkl"
modelo_path = os.path.join(BASE_DIR, NOMBRE_MODELO)

try:
    model = joblib.load(modelo_path)
    print(f"✅ Modelo '{NOMBRE_MODELO}' cargado exitosamente.")
except Exception as e:
    print(f"❌ Error crítico al cargar el modelo: {str(e)}")
    model = None

# 2. DEFINICIÓN DE FEATURES (Orden exacto del entrenamiento)
FEATURES_CORRECTAS = ['Rating', 'Size_MB', 'Price', 'Category_Encoded']

@app.route("/predice", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "El modelo no está cargado en el servidor"}), 500

    try:
        # Obtener datos del JSON enviado por API Tester
        data = request.get_json()
        if data is None:
            return jsonify({"error": "JSON no detectado o mal formado"}), 400

        # 3. CREACIÓN DEL DATAFRAME CON TIPOS DE DATOS OPTIMIZADOS
        # Nota: Category_Encoded se pasa como int para ser fiel al LabelEncoder
        df = pd.DataFrame([[
            float(data.get('Rating', 0)),
            float(data.get('Size_MB', 0)),
            float(data.get('Price', 0)),
            int(data.get('Category_Encoded', 0))
        ]], columns=FEATURES_CORRECTAS)

        # 4. PREDICCIÓN Y CÁLCULO DE PROBABILIDAD (Confianza)
        prediction = model.predict(df)[0]
        # predict_proba nos da [prob_clase_0, prob_clase_1]
        probabilidad_exito = model.predict_proba(df)[0][1]

        # 5. RESPUESTA ESTRUCTURADA PARA EL EMPRESARIO
        return jsonify({
            "App_Sera_Exito": bool(prediction),
            "Confianza_Prediccion": f"{probabilidad_exito * 100:.2f}%",
            "Clasificacion_Negocio": "Alta Probabilidad de >1M Descargas" if prediction == 1 else "Riesgo de Bajo Desempeño",
            "Message": "Análisis de viabilidad completado exitosamente"
        })
    
    except ValueError as ve:
        return jsonify({"error": f"Error en tipo de datos: {str(ve)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Error inesperado: {str(e)}"}), 500

# 6. EJECUCIÓN DEL SERVIDOR
if __name__ == "__main__":
    # Usamos 0.0.0.0 para que sea accesible desde otros dispositivos en la red si fuera necesario
    # El puerto 8000 es el que configuraste en tu API Tester
    print("🚀 Iniciando API de Predicción de Éxito Apps...")
    app.run(host='0.0.0.0', port=8000, debug=True)