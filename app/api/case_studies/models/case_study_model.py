from sqlalchemy import Column, Integer, String, Text
from app.db.base_class import Base


class CaseStudy(Base):
    id = Column(Integer, primary_key=True)
    article_id = Column(String(50))
    judgement = Column(Text)
    title = Column(String(200))
    content = Column(Text)
