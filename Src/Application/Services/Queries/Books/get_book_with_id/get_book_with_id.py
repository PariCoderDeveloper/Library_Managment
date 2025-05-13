from Domain.Interfaces.IBookRepository import IBookRepository
from DTO.get_book_with_id_dto import GetBookwithIdDTO

class GetBookwithIdQueryHandler:
    def __init__(self, book_repository : IBookRepository):
        self.book_repository = book_repository

    def execute(self, book_id:int) -> GetBookwithIdDTO:
        book = self.book_repository.get_book_by_id(book_id)
        return GetBookwithIdDTO(
                title= book.title,
                genre= book.genre,
                authors_name= [author.name for author in book.authors]
            )
        