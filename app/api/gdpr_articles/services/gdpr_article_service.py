from typing import Optional, List, Type, Union, Dict, Any

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.api.gdpr_articles.dto.gdpr_article_dto import GDPRArticleCreateDto, GDPRArticleUpdateDto
from app.api.gdpr_articles.models.gdpr_article_model import GDPRArticle
from app.api.gdpr_articles.services import BaseService


class GDPRArticleService(BaseService[GDPRArticle, GDPRArticleCreateDto, GDPRArticleUpdateDto]):

    def get_by_title(self, db: Session, *, title: str) -> Optional[GDPRArticle]:
        return db.query(GDPRArticle).filter(GDPRArticle.title == title).first()

    def get_all(self, db: Session) -> List[Type[GDPRArticle]]:
        return db.query(GDPRArticle).all()

    def get(self, db: Session, id: Any) -> Optional[GDPRArticle]:
        return db.query(GDPRArticle).filter(GDPRArticle.id == id).first()

    def create(self, db: Session, *, obj_in: GDPRArticleCreateDto) -> GDPRArticle:
        db_obj = GDPRArticle(
            article_number=obj_in.article_number,
            title=obj_in.title,
            content=obj_in.content,
            context=obj_in.context,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, *, id: int) -> GDPRArticle:
        obj = db.query(GDPRArticle).get(id)
        db.delete(obj)
        db.commit()
        return obj

    def update(
            self,
            db: Session,
            *,
            db_obj: GDPRArticle,
            obj_in: Union[GDPRArticleUpdateDto, Dict[str, Any]]
    ) -> GDPRArticle:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


gdprArticleService = GDPRArticleService(GDPRArticle)
