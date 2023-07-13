"""
Autor: Yohan Alfonso Hernandez
Fecha: 13-07-2023
Tema: creación de un post para llevar datos a mysql
"""

# install fastapi
#- pip3 install fastapi
# installuvicorn that is an ASGI web server implementation for Pytho
#- pip3 install uvicorn

from fastapi import FastAPI
from . import schemas

# Inicia la aplicación
app = FastAPI()

# Crea un Endpoint

@app.post("/API_PYTHON/")
def create_book(request:schemas.Book_Autor_Payload): #función de lleva datos a mysql 
    return "New book Added" + request.book.title + " " +str(request.book.number_of_pages) + "New Author Added" + request.author.first_name + " "\
            + " " + request.author.last_name
    
# ejecutar 
# E:\Python\Git_Repositories\api_python> uvicorn  books-api.post_end_point:app --reload 


