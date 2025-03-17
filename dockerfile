# Usa una imagen base de Python
FROM python:3.11

ARG DEBIAN_FRONTEND=noninteractive

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos
COPY . .

RUN apt-get update -q && \
    apt-get install -y -qq --no-install-recommends \
    xvfb \
    libxcomposite1 \
    libxdamage1 \
    libatk1.0-0 \
    libasound2 \
    libdbus-1-3 \
    libnspr4 \
    libgbm1 \
    libatk-bridge2.0-0 \
    libcups2 \
    libxkbcommon0 \
    libatspi2.0-0 \
    libnss3

# Instala las dependencias
RUN pip install -r requirements.txt && \
    playwright install chromium

# Expone el puerto
EXPOSE 8000

# Comando para ejecutar FastAPI
WORKDIR /app/src
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]