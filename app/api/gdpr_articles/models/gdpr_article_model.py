from sqlalchemy import Column, Integer, String
from app.db.base_class import Base


class GDPRArticle(Base):
    id = Column(Integer, primary_key=True)
    article_number = Column(String(50))
    title = Column(String(200))
