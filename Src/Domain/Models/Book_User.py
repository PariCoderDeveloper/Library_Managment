from Infrastructure.base import Base
from sqlalchemy import Table
from sqlalchemy import Column, Integer, Boolean, ForeignKey

book_user_assocation = Table(
    'book_user',
    Base.metadata,
    Column('book_id',Integer,ForeignKey('books.id')),
    Column('user_id',Integer, ForeignKey('users.id')),
    Column('deleted', Boolean, default=False)
)