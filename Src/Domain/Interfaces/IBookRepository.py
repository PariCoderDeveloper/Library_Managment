from abc import ABC, abstractmethod
from typing import List, Optional
from Domain.Models.Book_Author import Book

class IBookRepository(ABC):
    @abstractmethod
    def get_all_books(self) -> List[Book]:
        """Retrieve all books."""
        pass
    
    @abstractmethod
    def get_book_by_id(self, book_id:int) ->Optional[Book]:
        """Retrieve a book by its ID."""
        pass
    
    @abstractmethod
    def add_book(self, book: Book) -> None:
        """Add a new book."""
        pass
    
    @abstractmethod
    def update_book(self,book: Book) -> None:
        """Update an existing book."""
        pass
    
    @abstractmethod
    def delete_book(self, book_id:int) -> None:
        """Delete a book."""
        pass
    
    @abstractmethod
    def filter_book(self, genre: Optional[str], year: Optional[int], author_name: Optional[str]) -> List[Book]:
        """Filter books based on genre, year, and author."""
        pass