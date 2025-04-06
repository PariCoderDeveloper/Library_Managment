from abc import ABC, abstractmethod
from typing import List, Optional
from Domain.Models.User_Profile import User

class IUserRepository(ABC):
    @abstractmethod
    def get_all_users(self) -> List[User]:
        """Retrieve all users."""
        pass
    
    @abstractmethod
    def get_user_by_id(self, user_id:int) -> Optional[User]:
        """Retrive a user by its ID."""
        pass
    
    @abstractmethod
    def add_user(self, user:User) -> None:
        """Add a new user."""
        pass
    
    @abstractmethod
    def update_user(self, user:User) -> None:
        """Update an existing user."""
        pass
    
    @abstractmethod
    def delete_user(self, user_id:int) -> None:
        """Delete a user."""
        pass
    
    @abstractmethod
    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        """Authenticate a user by username and password."""
        pass