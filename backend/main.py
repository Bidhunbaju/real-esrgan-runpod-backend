from fastapi import FastAPI, UploadFile, File
import uuid, os
from upscale_worker import upscale_image

app = FastAPI()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/upscale")
async def upscale(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    input_path = f"{UPLOAD_DIR}/{file_id}.png"
    output_path = f"{OUTPUT_DIR}/{file_id}_upscaled.png"

    with open(input_path, "wb") as f:
        f.write(await file.read())

    final_path = upscale_image(input_path, output_path)

    return {"output_url": final_path}
