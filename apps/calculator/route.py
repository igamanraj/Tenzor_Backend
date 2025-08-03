from fastapi import APIRouter
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import Image
from PIL import Image

router = APIRouter()

@router.post("/analyze")
async def run(data: ImageData):
    image_data = base64.b64decode(data.image.split(",")[1])
    image_bytes = BytesIO(image_data)
    image = Image.open(image_bytes)
    responses = analyze_image(image, dict_of_vars=data.dict_of_vars)
    data = []
    for response in responses:
        data.append(response)
    print("response in return", response) # to test id response is coming 
    return{
        "message" : "Image analyzed successfully",
        "type": "success",
        "data": data
    }