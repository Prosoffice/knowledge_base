from typing import Optional

from pydantic import BaseModel


class CaseStudyBase(BaseModel):
    article_id: Optional[int] = None
    title: Optional[str] = None
    judgement: Optional[str] = None
    content: Optional[str] = None


class CaseStudyCreateDto(CaseStudyBase):
    article_id: int
    title: str
    content: str
    judgement: str


class CaseStudyUpdateDto(CaseStudyBase):
    pass


class CaseStudyInDbBase(CaseStudyBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class CaseStudy(CaseStudyInDbBase):
    pass

