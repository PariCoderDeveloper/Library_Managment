from Infrastructure.engine import Session
from Domain.Models.Book_Author import Author , Book , book_author_assocation
from Domain.Interfaces.IAuthorRepository import IAuthorRepository

class AuthorRepository(IAuthorRepository):
    def get_all_authors(self):
        with Session() as session:
            return session.query(Author).filter(Author.deleted == False).all()
    
    def get_author_by_id(self, author_id: int):
        with Session() as session:
            return session.query(Author).filter(Author.id == author_id, Author.deleted == False).first()
    
    def get_author_collabration(self, author_id):
        with Session() as session:
            session.query(Author).join(Author)
    
    def get_book_by_author(self, author_id):
        with Session() as session:
            return session.query(Book).filter(Book.authors.any(Author.id == author_id)).all()
    
    def add_author(self, author: Author):
        with Session() as session:
            session.add(author)
            session.commit()
            
    def delete_author(self, author_id:int):
        with Session() as session:
            author = session.query(Author).filter(Author.id == author_id).first()
            if author:
                author.deleted = True
                session.commit()
    
    def update_author(self, author:Author):
        with Session() as session:
            session.merge(author)   
            session.commit()