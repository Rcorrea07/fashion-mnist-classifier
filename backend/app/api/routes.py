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
        contents = await file.read()
        
        img_array = process_image(contents)
        
        result = predict_class(img_array)
        
        return result
        
    except ValueError as e:
        return {"erro": str(e)}
    except Exception as e:
        return {"erro": f"Ocorreu um erro interno: {str(e)}"}