# se usa la libreria pydianic para convertir schemas creados en clases a formato python
from pydantic import BaseModel

# se crean las clases que contienen los datos
class Book(BaseModel):
    title:str
    number_of_pages: int
    
class Author(BaseModel):
    first_name:str
    last_name:str
    
class Book_Autor_Payload(BaseModel):
    book:Book
    author:Author
    
    
