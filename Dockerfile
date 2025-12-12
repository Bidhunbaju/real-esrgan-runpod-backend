FROM runpod/base:3.0.0-cuda11.8

RUN apt-get update && apt-get install -y git wget

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN mkdir -p /app/backend/models/
RUN wget -O /app/backend/models/RealESRGAN_x4plus.pth \
    https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5/RealESRGAN_x4plus.pth

CMD ["python", "backend/main.py"]
