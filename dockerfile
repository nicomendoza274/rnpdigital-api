FROM mcr.microsoft.com/playwright/python:v1.50.0-jammy

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Instalar Chromium con sus dependencias
RUN playwright install chromium
RUN playwright install-deps chromium

# Configurar variable de entorno para que Playwright use el navegador instalado
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

EXPOSE 8000

WORKDIR /app/src
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]