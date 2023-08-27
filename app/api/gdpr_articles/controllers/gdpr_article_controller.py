from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any, List
from app.api.gdpr_articles.dto.gdpr_article_dto import GDPRArticle
from app.api.gdpr_articles.factories.db_factory import get_db
from app.api.gdpr_articles.services.gdpr_article_service import gdprArticleService

router = APIRouter()


@router.get("/gdpr_articles", response_model=List[GDPRArticle])
def read_gdpr_articles(db: Session = Depends(get_db)) -> Any:
    all_gdpr_articles = gdprArticleService.get_all(db=db)
    return all_gdpr_articles

