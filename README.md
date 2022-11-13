# Reto Python - HTTP Request - Redis - MongoDB
# Remake Reto NodeJS http & base de datos

## Instrucciones
- Instalar Python versión 3.
- Crear variable virtual en raíz del proyecto: ```python3 -m venv .venv```; donde ```.venv``` es el nombre de la variable virtual.
- Activar variable virtual: ```source .venv/bin/activate```; esto es necesario para correr el proyecto.
- Para activar variable virtual en windows OS: ```.venv\Scripts\activate```.
- - Para instalar dependencias/librerías: ```pip3 install -r requirements.txt ```  o ```pip install -r requirements.txt ``` .
- Para desactivar la variable virtual (en raíz del proyecto): ```deactivate```

## Para correr
- Escribir en la raíz del proyecto: ```python main.py ```


## Salida de sistema
- Visualizar código secreto obtenido y comparar la pista obtenida por medio de un endpoint.


## Adicionales
- HTTP Request en Python

## Bases de datos
- Redis
- Mongo DB 

## Funcionamiento
- Realiza solicitud http a un endpoint para obtener las credenciales de acceso a una BD en redis.
- Con las credenciales anteriores, toma credenciales para acceder a una colección en un cluster de MongoDB.
- Accede a la BD y a la colección objetivo para obtener el campo requerido referente al código.
- Decodifica y se visualiza el código secreto.


Continuación de Reto NodeJS - HTTP Requests -Bases de Datos \
[Enlace Reto](https://paper.dropbox.com/doc/Reto-de-Node-HTTP-y-Bases-de-Datos-p9dWNgBSNXj8ZpZfK9C60) \
[Enlace versión original](https://github.com/ht1204/reto-node) \
[Enlace versión remake Node+TS](https://github.com/ht1204/reto-node-v2)
