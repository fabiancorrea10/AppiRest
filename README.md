# AppiRest
Aplicacion Appi Rest que tiene como objetivo permitir consultas a un archivo biblioteca Json y cambios de la informacion del lenguaje del libro elegido
El entorno creado venv tiene descargado python 3.11, pip, uvicorn, FastApi, Json y request.
Para interactuar con un cliente, tenemos que tener abierto el archivo main en una pc utilizando el comando: uvicorn main:app -- host 0.0.0.0 --reload. De esta forma podemos exponer el host a la pantalla de otra pc. 
En otra pc, abrimos cliente, que debe tener previamente cargada en la variable url la ip de la pc donde esta main funcionando. Desde esta pantalla, nuestro cliente podra hacer consultas de la biblioteca o modificar el idioma de alguno de los textos, actualizando el archivo books.json.
