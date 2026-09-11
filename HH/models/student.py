from pydantic import BaseModel
from  models.cource import Cource
from uuid import UUID


class Student(BaseModel):
    id: UUID
    name: str
    age: int
    course: Cource

class StudentCreate(BaseModel):
    name: str
    age: int
    course: Cource