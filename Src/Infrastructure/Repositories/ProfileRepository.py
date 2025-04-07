from Infrastructure.engine import Session
from Domain.Models.User_Profile import Profile
from Domain.Interfaces.IProfileRepository import IProfileRepository

class ProfileRepository(IProfileRepository):
    def get_all_profiles(self):
        with Session() as session:
            return session.query(Profile).filter(Profile.deleted == False).all()
    
    def get_profile_by_id(self, profile_id: int):
        with Session() as session:
            return session.query(Profile).filter(Profile.id == profile_id).first()
    
    def add_profile(self, profile:Profile):
        with Session() as session:
            session.add(profile)
            session.commit()
    
    def update_profile(self, profile:Profile):
        with Session() as session:
            session.merge(profile)
            session.commit()
            
    def delete_profile(self, user_id:int):
        with Session() as session:
            profile = session.query(Profile).filter(Profile.id == user_id).first()
            if profile:
                profile.deleted = True
                session.commit()