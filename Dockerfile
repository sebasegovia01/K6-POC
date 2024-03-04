# Utiliza la imagen base de Python 3.10.13
FROM python:3.10.13

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt en el contenedor
COPY requirements.txt .

# Instala las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos del proyecto en el contenedor
COPY . .

# Expone el puerto 5000
EXPOSE 5000

# Comando para ejecutar la aplicación usando Uvicorn
CMD ["uvicorn", "requestPoc:app", "--host", "0.0.0.0", "--port", "5000"]
