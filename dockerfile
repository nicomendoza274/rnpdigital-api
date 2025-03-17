FROM mcr.microsoft.com/playwright/python:v1.50.0-jammy

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Instalar Chromium con sus dependencias y verificar la instalación
RUN playwright install chromium
RUN playwright install-deps chromium
RUN mkdir -p /usr/local/lib/python3.10/dist-packages/playwright/driver/package/.local-browsers/chromium_headless_shell-1155/chrome-linux/
RUN ln -s /ms-playwright/chromium-*/chrome-linux/chrome /usr/local/lib/python3.10/dist-packages/playwright/driver/package/.local-browsers/chromium_headless_shell-1155/chrome-linux/headless_shell

EXPOSE 8000

WORKDIR /app/src
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]