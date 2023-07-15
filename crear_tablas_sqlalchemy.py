from sqlalchemy import create_engine, select
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.orm import registry, Session, relationship


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
	first_name = Column(String(10))
	last_name = Column(String(10))
	def __repr__(self):
		return "<Author(author_id='{0}', first_name='{1}', last_name='{2}')>" \
			.format(self.author_id, self.first_name, self.last_name)


Base.metadata.create_all(engine)