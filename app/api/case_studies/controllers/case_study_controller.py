from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Any, List
from app.api.case_studies.dto.case_study_dto import CaseStudy, CaseStudyCreateDto, CaseStudyUpdateDto
from app.api.case_studies.factories.db_factory import get_db
from app.api.case_studies.services.case_study_service import caseStudyService
from app.core.security import auth_service
from app.core.utils import AuthUserDto

router = APIRouter()


@router.get("/case_studies", response_model=List[CaseStudy])
def read_case_studies(
        db: Session = Depends(get_db),
        current_user: AuthUserDto = Depends(auth_service)
) -> Any:
    all_case_studies = caseStudyService.get_all(db=db)
    return all_case_studies


@router.post("/case_studies", response_model=CaseStudy)
def create_case_study(
        *,
        db: Session = Depends(get_db),
        obj_in: CaseStudyCreateDto,
        current_user: AuthUserDto = Depends(auth_service)
) -> Any:
    new_case_study = caseStudyService.create(db, obj_in=obj_in)
    return new_case_study


@router.delete("/case_studies/{id}", response_model=str)
def delete_case_study(
        *,
        db: Session = Depends(get_db),
        id: int,
        current_user: AuthUserDto = Depends(auth_service)
) -> Any:
    deleted_case_study = caseStudyService.delete(db, id=id)
    if deleted_case_study:
        return f"Case Study {id} successfully deleted"
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not Delete Entry",
        )


@router.put("/case_studies/{id}", response_model=CaseStudy)
def update_case_study(
        *,
        db: Session = Depends(get_db),
        obj_in: CaseStudyUpdateDto,
        id: int,
        current_user: AuthUserDto = Depends(auth_service)
) -> Any:
    instance_model = caseStudyService.get(db, id)
    updated_case_study = caseStudyService.update(db=db, db_obj=instance_model, obj_in=obj_in)
    if updated_case_study:
        return updated_case_study
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not Update Entry",
        )
