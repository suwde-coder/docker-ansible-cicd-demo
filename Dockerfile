# Base image olarak Python 3.10 slim kullan
FROM python:3.10-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Önce gereksinim dosyasını kopyala (Docker cache optimizasyonu için)
COPY app/requirements.txt .

# Bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodlarının geri kalanını kopyala
COPY app/ .

# Uygulamanın çalışacağı 5000 portunu dışa aç
EXPOSE 5000

# Uygulamayı başlat
CMD ["python", "app.py"]
