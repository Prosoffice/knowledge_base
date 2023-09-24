from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Any, List
from app.api.regulations.dto.regulation_dto import Regulation, RegulationCreateDto, RegulationUpdateDto
from app.api.regulations.factories.db_factory import get_db
from app.api.regulations.services.regulation_service import regulationService
from app.core.security import auth_service
from app.core.utils import AuthUserDto

router = APIRouter()


@router.get("/regulations", response_model=List[Regulation])
def read_gdpr_articles(
        db: Session = Depends(get_db),
        current_user: AuthUserDto = Depends(auth_service)
) -> Any:
    all_regulations = regulationService.get_all(db=db)
    return all_regulations

@router.get("/regulations/{article_id}", response_model=List[Regulation])
def read_gdpr_articles(
        article_id: int,
        db: Session = Depends(get_db),
        current_user: AuthUserDto = Depends(auth_service)
) -> Any:
    all_regulations = regulationService.get_by_article(article_id, db=db)
    return all_regulations

@router.post("/regulations", response_model=Regulation)
def create_regulation(
        *,
        db: Session = Depends(get_db),
        obj_in: RegulationCreateDto,
        current_user: AuthUserDto = Depends(auth_service)
) -> Any:
    new_regulation = regulationService.create(db, obj_in=obj_in)
    return new_regulation


@router.delete("/regulations/{id}", response_model=str)
def delete_regulation(
        *,
        db: Session = Depends(get_db),
        id: int,
        current_user: AuthUserDto = Depends(auth_service)
) -> Any:
    deleted_regulation = regulationService.delete(db, id=id)
    if deleted_regulation:
        return f"Regulation {id} successfully deleted"
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not Update Entry",
        )


@router.put("/regulations/{id}", response_model=Regulation)
def update_regulation(
        *,
        db: Session = Depends(get_db),
        obj_in: RegulationUpdateDto,
        id: int,
        current_user: AuthUserDto = Depends(auth_service)
) -> Any:
    instance_model = regulationService.get(db, id)
    updated_regulation = regulationService.update(db=db, db_obj=instance_model, obj_in=obj_in)
    if updated_regulation:
        return updated_regulation
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not Update Entry",
        )
