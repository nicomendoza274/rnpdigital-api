# Usa una imagen base ligera con compatibilidad con Playwright
FROM mcr.microsoft.com/playwright/python:v1.50.0-jammy

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Asegúrate de instalar los navegadores de Playwright
RUN playwright install chromium


# Expone el puerto
EXPOSE 8000

# Comando para ejecutar FastAPI
WORKDIR /app/src
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
