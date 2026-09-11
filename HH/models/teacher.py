from pydantic import BaseModel
from  models.cource import Cource
from uuid import UUID


class Teacher(BaseModel):
    id: UUID
    name: str
    age: int
    course: Cource

class TeacherCreate(BaseModel):
    name: str
    age: int
    course: Cource