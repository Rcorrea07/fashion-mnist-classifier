# backend/app/api/routes.py
from fastapi import APIRouter, UploadFile, File
from app.services.image_service import process_image
from app.services.model_service import predict_class

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "API Fashion MNIST funcionando, super organizada!"}

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # 1. Lê os bytes do arquivo enviado
        contents = await file.read()
        
        # 2. Manda para o service de imagem processar
        img_array = process_image(contents)
        
        # 3. Manda para o service do modelo adivinhar
        result = predict_class(img_array)
        
        return result
        
    except ValueError as e:
        return {"erro": str(e)}
    except Exception as e:
        return {"erro": f"Ocorreu um erro interno: {str(e)}"}