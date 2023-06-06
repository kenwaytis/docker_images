from fastapi import FastAPI , status , HTTPException
from pydantic import BaseModel
from fer import FER
from loguru import logger
import json

detector = FER(mtcnn=True)

app = FastAPI()

class Image(BaseModel):
    image: str


@app.post("/fer", tags=["FER"], summary="Predict emotions in an image", response_description="Emotion detection results")
async def predict_image(items:Image):
    """
    Predicts emotions in an image using FER (Facial Emotion Recognition).

    - **items**: Request body containing the image in base64 format.
    - **returns**: Detected emotions in the image.

    """
    try:
        results = detector.detect_emotions(items.image)

        # max_emotion = max(results[0]['emotions'], key=results[0]['emotions'].get)
        # results[0]['max_emotion'] = max_emotion
        json_data = json.dumps(results)
        json_data = json_data.replace("'", '"')
        logger.info(json_data)
        return json_data
    except Exception as e:
        errors = str(e)
        mod_errors = errors.replace('"', '**').replace("'", '**')
        logger.error(mod_errors)
        message = {
            "err_no": "400",
            "err_msg": mod_errors
            }
        json_data = json.dumps(message)
        json_data = json_data.replace("'", '"')
        return json_data
        
@app.get("/health")
async def health_check():
    try:
        logger.info("health 200")
        return status.HTTP_200_OK

    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

@app.get("/health/inference")
async def health_check():
    try:
        results = detector.detect_emotions("/home/web_serving/test.jpg")
        logger.info("health 200")
        return status.HTTP_200_OK

    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


