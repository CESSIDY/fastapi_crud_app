from sqlalchemy import Column, VARCHAR
from sqlalchemy.dialects.mysql import BIGINT, TEXT
from src.models import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column("id", BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    title = Column(VARCHAR(768), index=True)
    content = Column(TEXT())
