from Domain.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String , ForeignKey

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True,autoincrement=True)
    username = Column(String, unique=True, nullable=True)
    
    profile = relationship("Profile",back_populates="user", uselist=False)

class Profile(Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key=True,autoincrement=True)
    bio = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user = relationship("User", back_populates="profile") 