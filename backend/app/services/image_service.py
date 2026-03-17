# backend/app/services/image_service.py
import cv2
import numpy as np

def process_image(contents: bytes) -> np.ndarray:
    """Transforma os bytes da imagem em um array normalizado para o modelo."""
    # Converte bytes para array numpy
    npimg = np.frombuffer(contents, np.uint8)
    
    # Decodifica em escala de cinza
    img = cv2.imdecode(npimg, cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        raise ValueError("Não foi possível abrir a imagem.")

    # Redimensiona para 28x28 (tamanho que o Fashion MNIST exige)
    img = cv2.resize(img, (28, 28))
    
    # Normaliza as cores (de 0-255 para 0.0-1.0)
    img = img / 255.0
    
    # Adiciona as dimensões de canal e batch (fica no formato [1, 28, 28, 1])
    img = np.expand_dims(img, axis=-1)
    img = np.expand_dims(img, axis=0)
    
    return img