"""
Autor: Yohan Alfonso Hernandez
Fecha: 13-07-2023
Tema: creación de api con la libreria FastAPI
"""

# install fastapi
#- pip3 install fastapi
# installuvicorn that is an ASGI web server implementation for Pytho
#- pip3 install uvicorn
from . import schemas
from fastapi import FastAPI

# Inicia la aplicación
app = FastAPI()

# Crea un Endpoint

@app.get("/") # el "/" es el home
def  get_root(): # hacer una peticion de get para retorno de información
    return" este el api de books" # para ejecutr esta parte se necesita uvicorn

    """
    desde el home: uvicorn  books-api.main:app --reload
    en la salida entrega el servidor http://127.0.0.1:8000
    http://127.0.0.1:8000/docs para ver la documentación de la api se agrega /docs en el browser
    
    """


@app.post("/API_PYTHON/")
def create_book(request:schemas.Book_Autor_Payload): #función de lleva datos a mysql 
    return "New book Added" + request.book.title + " " +str(request.book.number_of_pages) + "New Author Added" + request.author.first_name + " "\
            + " " + request.author.last_name
    
# ejecutar 
# E:\Python\Git_Repositories\api_python> uvicorn  books-api.main:app --reload  

    """desde postaman se hace un post con la siguiente información:
    Conexión: 127.0.0.1:8000/API_PYTHON/
    
    en el bodyu:
    
    
    {
	"book":{
		"title": "The hunters",
		"number_of_pages": 560
	},
	"author":{
		"first_name":"Kate",
		"last_name": "Quinn"
	}
}
    """

