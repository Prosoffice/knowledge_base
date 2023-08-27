from typing import Generic, TypeVar, Type

from pydantic import BaseModel

from user_management.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateDtoType = TypeVar("CreateDtoType", bound=BaseModel)
UpdateDtoType = TypeVar("UpdateDtoType", bound=BaseModel)


class BaseService(Generic[ModelType, CreateDtoType, UpdateDtoType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model