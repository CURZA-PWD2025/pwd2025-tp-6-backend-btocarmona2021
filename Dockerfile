# Imagen base oficial de Python
FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar requirements.txt y luego instalar dependencias
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de archivos de la app
COPY . .

# Exponer puerto 5000 (donde corre Flask)
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]
