# backend/app/services/model_service.py
import os
import numpy as np
import tensorflow as tf
from app.core.config import LABELS

# Caminho absoluto para achar o model.h5 sem erro
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_PATH = os.path.join(BASE_DIR, "model", "model.h5")

# Carrega o modelo na memória apenas uma vez quando o servidor inicia
model = tf.keras.models.load_model(MODEL_PATH)

def predict_class(image_array: np.ndarray) -> dict:
    """Passa a imagem pelo modelo e retorna a classe e as probabilidades."""
    predictions = model.predict(image_array)
    class_index = int(np.argmax(predictions))
    
    return {
        "classe": class_index,
        "label": LABELS[class_index],
        "probabilidades": predictions.tolist()
    }