# LibrosAPI
## API de FastAPI con SQLModel
Ejemplo de una API para gestionar Autores y Libros con una base de datos SQLite.

### Construir la imagen de Docker
En el directorio raíz de tu proyecto (donde se encuentra el archivo `Dockerfile`), ejecuta el siguiente comando para construir la imagen Docker:
```bash
docker build -t empleados_api .
```


### Ejecutar el contenedor Docker
Utilizando sqlite:
```bash
docker run -d -p 8000:8000 empleados_api
```

### Persistencia. 
La API puede guardar imagenes para empleados.
Si se elimina el contenedor o es reproducido, estas se perderán.
## Lograr la persistencia para imagenes.
- El Dockerfile actual las imágenes se guardan mientras el contenedor exista.
Dentro del _Dockerfile_ agregar:
```
VOLUME /code/app/media
```
- Docker debería de crear un volumen anónimo dentro de host.
- O levanta un _Volumen explícito_ :
```
docker volume create empleados_media
docker run -p 8000:8000 --env-file .env -v empleados_media:/code/app/media empleados_api
```
