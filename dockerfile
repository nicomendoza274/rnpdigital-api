# Imagen base ligera
FROM python:3.10-slim

# Instalar dependencias del sistema necesarias para Chromium
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libnss3 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libgtk-4-1 \
    libgraphene-1.0-0 \
    libgstreamer-gl1.0-0 \
    libgstreamer-plugins-bad1.0-0 \
    libavif15 \
    libenchant-2-2 \
    libsecret-1-0 \
    libmanette-0.2-0 \
    libgles2 \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python y Playwright
RUN pip install fastapi uvicorn playwright && playwright install chromium

# Crear un usuario sin privilegios
RUN useradd -m appuser
USER appuser

# Directorio de trabajo
WORKDIR /app

# Copiar el código
COPY . .

# Exponer el puerto
EXPOSE 8000

# Comando para ejecutar FastAPI

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
