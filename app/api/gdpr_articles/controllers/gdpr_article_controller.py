from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Any, List
from app.api.gdpr_articles.dto.gdpr_article_dto import GDPRArticle, GDPRArticleCreateDto, GDPRArticleUpdateDto
from app.api.gdpr_articles.factories.db_factory import get_db
from app.api.gdpr_articles.services.gdpr_article_service import gdprArticleService
from app.core.security import auth_service
from app.core.utils import AuthUserDto

router = APIRouter()


@router.get("/gdpr_articles", response_model=List[GDPRArticle])
def read_gdpr_articles(
        db: Session = Depends(get_db),
        current_user: AuthUserDto = Depends(auth_service)
) -> Any:
    all_gdpr_articles = gdprArticleService.get_all(db=db)
    return all_gdpr_articles

@router.get("/gdpr_articles/{id}", response_model=GDPRArticle)
def read_gdpr_articles(
        id: int,
        db: Session = Depends(get_db),
        current_user: AuthUserDto = Depends(auth_service)
) -> Any:
    gdpr_article = gdprArticleService.get(db=db, id=id)
    return gdpr_article

@router.post("/gdpr_articles", response_model=GDPRArticle)
def create_gdpr_article(
        *,
        db: Session = Depends(get_db),
        obj_in: GDPRArticleCreateDto,
        current_user: AuthUserDto = Depends(auth_service)
) -> Any:
    new_article = gdprArticleService.create(db, obj_in=obj_in)
    return new_article


@router.delete("/gdpr_articles/{id}", response_model=str)
def delete_article(
        *,
        db: Session = Depends(get_db),
        id: int,
        current_user: AuthUserDto = Depends(auth_service)
) -> Any:
    deleted_article = gdprArticleService.delete(db, id=id)
    if deleted_article:
        return f"Article {id} successfully deleted"
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not Update Entry",
        )


@router.put("/gdpr_articles/{id}", response_model=GDPRArticle)
def update_article(
        *,
        db: Session = Depends(get_db),
        obj_in: GDPRArticleUpdateDto,
        id: int,
        current_user: AuthUserDto = Depends(auth_service)
) -> Any:
    instance_model = gdprArticleService.get(db, id)
    updated_article = gdprArticleService.update(db=db, db_obj=instance_model, obj_in=obj_in)
    if updated_article:
        return updated_article
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not Update Entry",
        )
