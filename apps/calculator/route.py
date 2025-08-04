from fastapi import APIRouter, HTTPException
import base64
import logging
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import Image
from PIL import Image as PILImage

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/analyze")
async def run(data: Image):
    try:
        # Decode the base64 image
        image_data = base64.b64decode(data.image.split(",")[1])
        image_bytes = BytesIO(image_data)
        image = PILImage.open(image_bytes)
        
        # Analyze the image
        responses = analyze_image(image, dict_of_vars=data.dict_of_vars)
        
        data = []
        for response in responses:
            data.append(response)
            logger.info(f"Response in return: {response}")
            
        return {
            "message": "Image analyzed successfully",
            "type": "success",
            "data": data
        }
    except Exception as e:
        logger.error(f"Error analyzing image: {e}")
        raise HTTPException(status_code=500, detail=f"Error analyzing image: {str(e)}")