# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Instala los navegadores de Playwright
RUN apt-get update && apt-get install -y ffmpeg
RUN playwright install

# Expone el puerto
EXPOSE 8000

# Comando para ejecutar FastAPI
WORKDIR /app/src
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]