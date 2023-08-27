from typing import Optional, List, Type
from sqlalchemy.orm import Session
from app.api.gdpr_articles.dto.gdpr_article_dto import GDPRArticleCreateDto, GDPRArticleUpdateDto
from app.api.gdpr_articles.models.gdpr_article_model import GDPRArticle
from app.api.gdpr_articles.services import BaseService


class GDPRArticleService(BaseService[GDPRArticle, GDPRArticleCreateDto, GDPRArticleUpdateDto]):

    def get_by_title(self, db: Session, *, title: str) -> Optional[GDPRArticle]:
        return db.query(GDPRArticle).filter(GDPRArticle.title == title).first()

    def get_all(self, db: Session) -> List[Type[GDPRArticle]]:
        return db.query(GDPRArticle).all()


gdprArticleService = GDPRArticleService(GDPRArticle)
