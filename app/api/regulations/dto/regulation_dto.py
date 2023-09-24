from typing import Optional

from pydantic import BaseModel


class RegulationBase(BaseModel):
    article_id: Optional[int] = None
    title: Optional[str] = None
    content: Optional[str] = None


class RegulationCreateDto(RegulationBase):
    article_id: int
    title: str
    content: str


class RegulationUpdateDto(RegulationBase):
    ...


class RegulationInDbBase(RegulationBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class Regulation(RegulationInDbBase):
    ...

