from typing import List

from pydantic import BaseModel


class UserQuery(BaseModel):
    question: str


class UserMemory(BaseModel):
    ingredients: List[str]
    cocktails: List[str]
