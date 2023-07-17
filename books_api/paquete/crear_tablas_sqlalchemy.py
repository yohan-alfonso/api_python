from sqlalchemy import create_engine, select
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, ForeignKey, select
from sqlalchemy.orm import registry, relationship, Session


# DEFINE THE DATABASE CREDENTIALS
user = 'root'
password = 'yohan'
host = '127.0.0.1'
port = 3306
database = 'load_data_api'

# Create a connection to the MySQL database
engine = create_engine(f'mysql://{user}:{password}@{host}:{port}/{database}')

mapper_registry = registry()
Base = mapper_registry.generate_base()

class Author(Base):
	__tablename__ = 'authors'
	author_id = Column(Integer, primary_key=True)
	first_name = Column(String(20))
	last_name = Column(String(20))
	def __repr__(self):
		return "<Author(author_id='{0}', first_name='{1}', last_name='{2}')>" \
			.format(self.author_id, self.first_name, self.last_name)


class Book(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    title = Column(String(20))
    number_of_pages = Column(Integer)
    def __repr__(self):
        return "<Book(book_id='{0}', title='{1}', number_of_pages='{2}')>" \
			.format(self.book_id, self.title, self.number_of_pages)

class BookAuthor(Base):
    __tablename__ = 'bookauthors'
    bookauthor_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.author_id'))
    book_id = Column(Integer, ForeignKey('books.book_id'))

    author = relationship("Author")
    book = relationship("Book")

    def __repr__(self):
        return "<BookAuthor (bookauthor_id='{0}', author_id='{1}', book_id='{2}', first_name='{3}', last_name='{4}', title='{5}')>" \
			.format(self.bookauthor_id, self.author_id, self.book_id, self.author.first_name, self.author.last_name, self.book.title)   

Base.metadata.create_all(engine)

# Agregar información a las tablas por medio de postman
def add_book(book:Book, author:Author):
    with Session(engine) as session:
        existing_book= session.execute(select(Book).filter(Book.title==book.title , Book.number_of_pages==book.number_of_pages )).scalar()
        if existing_book is not None:
            print("Book has already been added")
            return
        print("The book doesn't need to be added")
        session.add(book)
        
        existing_author = session.execute(select(Author).filter(Author.first_name==author.first_name, Author.last_name==author.last_name)).scalar()
        if existing_author is not None:
            print("Author exists! Not adding author")
            session.flush()
            pairing=BookAuthor(author_id=existing_author.author_id, book_id=book.book_id)
        else:
            print("Author does not exist. Adding author")
            session.add(author)
            session.flush()
            pairing = BookAuthor(author_id=author.author_id, book_id=book.book_id)
        
        session.add(pairing)
        session.commit()
        print("New pairing added!" + str(pairing))
        
        
def get_book(book_id: int):
    with Session(engine) as session:
        book =  session.execute(select(Book).filter(Book.book_id == book_id)).scalar()
        if book is None:
            raise Exception("El libro no existe ")
        pairing = session.execute(select(BookAuthor).filter(BookAuthor.book_id==book_id)).scalar()
        author =  session.execute(select(Author).filter(Author.author_id== pairing.book_id)).scalar()
        return (book, author)
        