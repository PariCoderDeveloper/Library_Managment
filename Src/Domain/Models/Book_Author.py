from Domain.Models.Mixin.softDeleteMixin import softDeletionMixin
from Infrastructure.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer, String, Boolean, ForeignKey, Table

book_author_assocation = Table(
    'book_author',
    Base.metadata,
    Column("book_id",Integer,ForeignKey("books.id")),
    Column("author_id", Integer, ForeignKey("authors.id")),
    Column("deleted", Boolean, default=False)
)

class Book(Base, softDeletionMixin):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    year = Column(String)
    
    authors = relationship("Author",secondary=book_author_assocation ,back_populates="books")
    
class Author(Base, softDeletionMixin):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    deleted = Column(Boolean, default=False)
    
    books = relationship("Book", secondary=book_author_assocation, back_populates="authors")
