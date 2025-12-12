import torch
from realesrgan import RealESRGANer
from PIL import Image
import requests
from io import BytesIO

MODEL_PATH = "/app/backend/models/RealESRGAN_x4plus.pth"

def upscale_image(image_url, mode="4x"):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content)).convert("RGB")

    model = RealESRGANer(
        model_path=MODEL_PATH,
        scale=4,
        tile=200,
        tile_pad=10,
        pre_pad=0,
        half=torch.cuda.is_available()
    )

    output, _ = model.enhance(img)
    output_path = "/app/output.png"
    output.save(output_path)

    return output_path
