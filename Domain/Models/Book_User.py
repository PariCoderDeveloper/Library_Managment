from Domain.base import Base
from sqlalchemy import Table
from sqlalchemy import Column, Integer, ForeignKey

book_user_assocation = Table(
    'book_user',
    Base.metadata,
    Column('book_id',Integer,ForeignKey('books.id')),
    Column('user_id',Integer, ForeignKey('users.id'))
)