FROM runpod/base:3.0.0-cuda11.8

# Install dependencies
RUN apt-get update && apt-get install -y git wget

WORKDIR /app

# Copy backend files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Download Real-ESRGAN model automatically
RUN mkdir -p /app/models/
RUN wget -O /app/models/RealESRGAN_x4plus.pth \
    https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5/RealESRGAN_x4plus.pth

CMD ["python", "main.py"]

