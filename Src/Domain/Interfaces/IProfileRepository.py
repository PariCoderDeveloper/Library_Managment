from abc import ABC, abstractmethod
from typing import List, Optional
from Domain.Models.User_Profile import Profile

class IProfileRepository(ABC):
    @abstractmethod
    def get_all_profiles(self) -> List[Profile]:
        """Retrieve all profiles."""
        pass
    
    @abstractmethod
    def get_profile_by_user_id(self, user_id: int) -> Optional[Profile]:
        """Retrieve a profile by user ID."""
        pass
    
    @abstractmethod
    def add_profile(self, profile: Profile) -> None:
        """Add a new profile."""
        pass
    
    @abstractmethod
    def update_profile(self, profile: Profile) -> None:
        """Update an existing profile."""
        pass
    
    @abstractmethod
    def delete_profile(self, user_id: int) -> None:
        """Delete a profile by user ID."""
        pass
    