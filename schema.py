from pydantic import BaseModel

class Image(BaseModel):
    image : str  # Base64 encoded image string
    dict_of_vars: dict  # Dictionary of variables for the image analysis