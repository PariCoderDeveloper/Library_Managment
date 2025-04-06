from sqlalchemy import Column, Boolean

class softDeletionMixin:
    deleted = Column(Boolean, default=False)
