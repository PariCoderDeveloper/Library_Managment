from abc import ABC, abstractmethod
from typing import List, Optional
from Domain.Models.Book_Author import Book, Author

class IAuthorRepository(ABC):
    @abstractmethod
    def get_all_authors(self) -> List[Author]:
      """Retrieves all authors from the repository."""
      pass
  
    @abstractmethod
    def get_author_by_id(self, author_id: int) -> Optional[Author]:
        """Retrieves an author by their ID."""
        pass
    
    @abstractmethod
    def add_author(self, author: Author) -> None:
        """Adds a new author to the repository."""
        pass
    
    @abstractmethod
    def delete_author(self, author_id: int) -> None:
        """Deletes an author by their ID."""
        pass
    
    @abstractmethod
    def update_author(self, author: Author) -> None:
        """Updates an existing author."""
        pass
    
    @abstractmethod
    def get_book_by_author(self, author_id: int) -> List[Book]:
        """Retrieves all books written by a specific author."""
        pass
    
    @abstractmethod
    def get_author_collabration(self, author_id: int) -> List[Author]:
        """Retrieves all authors that have collaborated with a specific author."""
        pass