# Utiliza la imagen base de Python proporcionada por AWS para Lambda
FROM public.ecr.aws/lambda/python:3.10

# Establece el directorio de trabajo en el contenedor
WORKDIR ${LAMBDA_TASK_ROOT}

# Copia el archivo requirements.txt en el contenedor
COPY requirements.txt .

# Instala las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos del proyecto en el contenedor
COPY . .

# Instala Mangum para adaptar ASGI a Lambda
RUN pip install mangum

# Define la función handler para Lambda (asumiendo que `requestPoc.handlerp` es tu aplicación FastAPI)
CMD ["requestPoc.handler"]
