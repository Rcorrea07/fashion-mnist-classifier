import cv2
import numpy as np

def process_image(contents: bytes) -> np.ndarray:
    npimg = np.frombuffer(contents, np.uint8)
    
    img = cv2.imdecode(npimg, cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        raise ValueError("Não foi possível abrir a imagem.")

    img = cv2.resize(img, (28, 28))
    
    img = img / 255.0
    
    img = np.expand_dims(img, axis=-1)
    img = np.expand_dims(img, axis=0)
    
    return img