from sqlalchemy import Column, Integer, String, Text
from app.db.base_class import Base


class GDPRArticle(Base):
    id = Column(Integer, primary_key=True)
    article_number = Column(String(50))
    title = Column(String(200))
    content = Column(Text)
    context = Column(String(100))
