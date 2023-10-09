# fast-api-curso
Curso de FastAPI: Introducción, Operaciones, Validaciones y Autenticación

## Docker

Se sugiere hacer el desarrollo de todas las practicas usando *Docker* tal y como se indica en el archivo de buenas practicas.

```sh
docker compose build
docker compose up
```
Si quiere levantar el servicio en modo detach:
```sh
docker compose up -d
```

Los cambios que realizes dentro del contexto de build, se veran reflejados en la aplicacion. 

Abre una ventana del navegador en el puerto 5000 de tu maquina:

**http://localhost:5000/** 

### Optimizando la imagen de docker

Ve al directorio **my-api-alpine** y vuelve a construir la imagen y a levantar el servicio como indique anteriormente. 

Si vas a correr una terminal dentro de *alpine* no uses *bash* sino *sh*, por ejemplo:

```sh
docker compose up -d
docker exec -it 188284c444bb sh
```
