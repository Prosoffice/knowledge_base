from typing import Optional

from pydantic import BaseModel


class GDPRArticleBase(BaseModel):
    article_number: Optional[str] = None
    title: Optional[str] = None


class GDPRArticleCreateDto(GDPRArticleBase):
    article_number: str
    title: str


class GDPRArticleUpdateDto(GDPRArticleBase):
    ...


class GDPRArticleInDbBase(GDPRArticleBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class GDPRArticle(GDPRArticleInDbBase):
    ...

