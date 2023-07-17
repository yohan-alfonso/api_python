"""
Autor: Yohan Alfonso Hernandez
Fecha: 13-07-2023
Tema: creación de api con la libreria FastAPI
"""

# install fastapi
#- pip3 install fastapi
# installuvicorn that is an ASGI web server implementation for Pytho
#- pip3 install uvicorn

from fastapi import FastAPI, HTTPException
from . import schemas
from . import crear_tablas_sqlalchemy

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
# Para traer valores des una base de datos
@app.get("/API_PYTHON/{book_id}")
def retrive_book(book_id:int):
    try:
        return crear_tablas_sqlalchemy.get_book(book_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code= 404, detail = repr (e))
    

@app.post("/API_PYTHON/")
def create_book(request:schemas.Book_Autor_Payload): #función de lleva datos a mysql 
    crear_tablas_sqlalchemy.add_book(convert_into_book_model(request.book), covert_into_author_model(request.author)) # llama el modulo que crea y llena las tablas en la base de datos
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

# integrar la api con bases de datos en este caso MYSQL 
# primero se debe convertir el request schema en el fomato de eschema de base de datos
def convert_into_book_model(book:schemas.Book):
    return crear_tablas_sqlalchemy.Book(title=book.title, number_of_pages=book.number_of_pages) # instancia la función Book del modulo

def covert_into_author_model(author:schemas.Author):
    return crear_tablas_sqlalchemy.Author(first_name=author.first_name, last_name=author.last_name)



