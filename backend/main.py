import runpod
from upscale_worker import upscale_image

def handler(job):
    input_data = job["input"]
    image_url = input_data["image"]
    mode = input_data.get("mode", "4x")
    return upscale_image(image_url, mode)

runpod.serverless.start({"handler": handler})
