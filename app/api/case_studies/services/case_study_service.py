from typing import Optional, List, Type, Union, Dict, Any

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.api.case_studies.dto.case_study_dto import CaseStudyUpdateDto, CaseStudyCreateDto
from app.api.case_studies.models.case_study_model import CaseStudy
from app.api.case_studies.services import BaseService


class CaseStudyService(BaseService[CaseStudy, CaseStudyCreateDto, CaseStudyUpdateDto]):

    def get_by_title(self, db: Session, *, title: str) -> Optional[CaseStudy]:
        return db.query(CaseStudy).filter(CaseStudy.title == title).first()

    def get_all(self, db: Session) -> List[Type[CaseStudy]]:
        return db.query(CaseStudy).all()

    def get(self, db: Session, id: Any) -> Optional[CaseStudy]:
        return db.query(CaseStudy).filter(CaseStudy.id == id).first()

    def create(self, db: Session, *, obj_in: CaseStudyCreateDto) -> CaseStudy:
        db_obj = CaseStudy(
            article_id=obj_in.article_id,
            title=obj_in.title,
            content=obj_in.content,
            judgement=obj_in.judgement,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, *, id: int) -> CaseStudy:
        obj = db.query(CaseStudy).get(id)
        db.delete(obj)
        db.commit()
        return obj

    def update(
            self,
            db: Session,
            *,
            db_obj: CaseStudy,
            obj_in: Union[CaseStudyUpdateDto, Dict[str, Any]]
    ) -> CaseStudy:
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


caseStudyService = CaseStudyService(CaseStudy)
