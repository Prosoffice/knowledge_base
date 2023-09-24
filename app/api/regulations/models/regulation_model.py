from sqlalchemy import Column, Integer, String, Text
from app.db.base_class import Base


class Regulation(Base):
    id = Column(Integer, primary_key=True)
    article_id = Column(Integer)
    content = Column(Text)
