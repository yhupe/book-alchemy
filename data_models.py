from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.orm import sessionmaker, relationship


# Create a database connection
engine = create_engine('sqlite:///data/library.sqlite')

# Create a database session
Session = sessionmaker(bind=engine)
session = Session()

db = SQLAlchemy()

class Author(db.Model):
    """Class inherits from db.Model and defines the structure of the database table 'authors'.
    Also serves as abstraction layer for interaction between python and the database itself in
    a more object-oriented way."""

    __tablename__ = 'authors'

    author_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    birthdate = Column(String)
    date_of_death = Column(String)

    def __repr__(self):
        return f"Author: {self.name} - ID: {self.author_id})"

    # Relationship to the books (1:N)
    books = relationship('Book', back_populates='author', cascade="all, delete-orphan")


class Book(db.Model):
    """Class inherits from db.Model and defines the structure of the database table 'books'.
        Also serves as abstraction layer for interaction between python and the database itself in
        a more object-oriented way."""

    __tablename__ = 'books'

    book_id = Column(Integer, primary_key=True, autoincrement=True)
    ISBN = Column(Integer)
    title = Column(String)
    publication_year = Column(String)
    author_id = Column(Integer, ForeignKey('authors.author_id'))

    def __repr__(self):
        return f"Book title: {self.title} - ISBN: {self.ISBN})"

    # Relationship to the author (N:1)
    author = relationship('Author', back_populates='books')
