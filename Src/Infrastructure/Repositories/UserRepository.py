from Infrastructure.engine import Session
from Domain.Models.User_Profile import User
from Domain.Interfaces.IUserRepository import IUserRepository

class UserRepository(IUserRepository):
    def get_all_users(self):
        with Session() as session:
            return session.query(User).all()
    
    def get_user_by_id(self, user_id):
        with Session() as session:
            return session.query(User).filter(User.id == user_id).first()
    
    def add_user(self, user:User):
        with Session() as session:
            session.add(user)
            session.commit()
    
    def update_user(self, user:User):
        with Session() as session:
            session.merge(user)
            session.commit()
    
    def delete_user(self, user_id:int):
        with Session() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                user.deleted = True
                session.commit()
    
    def authenticate_user(self, username, password):
        return super().authenticate_user(username, password)