import os
import numpy as np
import tensorflow as tf
from app.core.config import LABELS

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_PATH = os.path.join(BASE_DIR, "model", "model.h5")

model = tf.keras.models.load_model(MODEL_PATH)

def predict_class(image_array: np.ndarray) -> dict:
    predictions = model.predict(image_array)
    class_index = int(np.argmax(predictions))
    
    return {
        "classe": class_index,
        "label": LABELS[class_index],
        "probabilidades": predictions.tolist()
    }