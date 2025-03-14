# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Instala los navegadores de Playwright
RUN playwright install --with-deps chromium firefox webkit

# Expone el puerto
EXPOSE 8000

# Comando para ejecutar FastAPI
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]