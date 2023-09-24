from typing import Optional, List, Type, Union, Dict, Any
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.api.regulations.dto.regulation_dto import RegulationCreateDto, RegulationUpdateDto
from app.api.regulations.models.regulation_model import Regulation
from app.api.regulations.services import BaseService


class RegulationService(BaseService[Regulation, RegulationCreateDto, RegulationUpdateDto]):

    def get_all(self, db: Session) -> List[Type[Regulation]]:
        return db.query(Regulation).all()

    def get(self, db: Session, id: Any) -> Optional[Regulation]:
        return db.query(Regulation).filter(Regulation.id == id).first()

    def create(self, db: Session, *, obj_in: RegulationCreateDto) -> Regulation:
        db_obj = Regulation(
            article_id=obj_in.article_id,
            title=obj_in.title,
            content=obj_in.content,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, *, id: int) -> Regulation:
        obj = db.query(Regulation).get(id)
        db.delete(obj)
        db.commit()
        return obj

    def get_by_article(self, article_id: int, db: Session) -> List[Type[Regulation]]:
        return db.query(Regulation).filter(Regulation.article_id == article_id).all()

    def update(
            self,
            db: Session,
            *,
            db_obj: Regulation,
            obj_in: Union[RegulationUpdateDto, Dict[str, Any]]
    ) -> Regulation:
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


regulationService = RegulationService(Regulation)
