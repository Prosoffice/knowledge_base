from typing import Optional

from pydantic import BaseModel, EmailStr


class GDPRArticleBase(BaseModel):
    article_number: Optional[str] = None
    title: Optional[str] = None
    content: Optional[str] = None
    context: Optional[str] = None


class GDPRArticleCreateDto(GDPRArticleBase):
    article_number: str
    title: str
    content: str
    context: str


class GDPRArticleUpdateDto(GDPRArticleCreateDto):
    ...


class GDPRArticleInDbBase(GDPRArticleBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class GDPRArticle(GDPRArticleInDbBase):
    ...

