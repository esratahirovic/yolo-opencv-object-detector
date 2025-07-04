# Temel görüntü (PyTorch + CUDA destekli)
FROM python:3.10

# Gerekli paketleri yükle
RUN apt-get update && apt-get install -y \
    ffmpeg libsm6 libxext6 libgl1-mesa-glx git \
    && rm -rf /var/lib/apt/lists/*

# Çalışma dizinini oluştur
WORKDIR /app

# Kodları kopyala
COPY . .

# Bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# YOLO font sorunu için Arial indir
RUN mkdir -p /root/.config/Ultralytics && \
    wget -O /root/.config/Ultralytics/Arial.ttf https://ultralytics.com/assets/Arial.ttf

# Default çalışacak komut
CMD ["python", "detect_and_log.py"]
