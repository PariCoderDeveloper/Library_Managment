from dataclasses import dataclass

@dataclass
class GetAllBooksQueryDTO:
    book_id : int
    title : str
    genre : str
    authors_name : list[str]