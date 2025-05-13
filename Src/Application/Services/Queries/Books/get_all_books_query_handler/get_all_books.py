from Domain.Interfaces.IBookRepository import IBookRepository
from DTO.get_all_books_query_dto import GetAllBooksQueryDTO

class GetAllBooksQueryHandler:
    def __init__(self, book_repository:IBookRepository):
        self.book_repository = book_repository

    def execute(self) -> list[GetAllBooksQueryDTO]:
        books = self.book_repository.get_all_books()
        return [
            GetAllBooksQueryDTO(
                book_id = book.id,
                title= book.title,
                genre= book.genre,
                author_name= [author.name for author in book.authors]
            ) for book in books
        ]