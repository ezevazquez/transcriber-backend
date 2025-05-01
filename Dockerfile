FROM python:3.10

# Instalar ffmpeg para pydub
RUN apt-get update && apt-get install -y ffmpeg

WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Exponer el puerto correcto para Render
ENV PORT 10000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
