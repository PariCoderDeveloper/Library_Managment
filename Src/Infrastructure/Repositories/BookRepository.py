from Infrastructure.engine import Session
from Domain.Models.Book_Author import Book
from Domain.Interfaces.IBookRepository import IBookRepository

class BookRepository(IBookRepository):   
    def get_all_books(self, genre= None, year=None, author_name=None):
        with Session() as session:
            query = session.query(Book)
            if genre:
                query.filter(Book.genre == genre)
            if year:
                query.filter(Book.year == year)
            if author_name:
                query.filter(Book.authors.has(author_name))
            return query.all()
    
    def get_book_by_id(self, book_id:int):
        with Session() as session:
            return session.query(Book).filter(Book.id == book_id).first()
    
    def add_book(self, book:Book):
        with Session() as session:
            session.add(book)
            session.commit()
    
    def update_book(self, book:Book):
        with Session() as session:
            session.merge(book)
            session.commit()
    
    def delete_book(self, book_id:int):
        with Session() as session:
           book = session.query(Book).filter(Book.id == book_id).first()
           if book:
               book.deleted = True
               session.commit()