FROM runpod/base:3.0.0-cuda11.8

# Install system deps
RUN apt-get update && apt-get install -y git wget

WORKDIR /app

# Copy project files
COPY . .

# Install Python deps
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Download Real-ESRGAN Model
RUN mkdir -p /app/backend/models/
RUN wget -O /app/backend/models/RealESRGAN_x4plus.pth \
    https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5/RealESRGAN_x4plus.pth

CMD ["python", "backend/main.py"]
