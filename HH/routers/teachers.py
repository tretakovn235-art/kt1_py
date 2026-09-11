from fastapi import APIRouter
import uuid
from typing import List
from models.teacher import Teacher, TeacherCreate
from database import teachers_db

router = APIRouter(prefix="/teachers")


@router.post("/", response_model=Teacher)
def create_teacher(teacher: TeacherCreate):
    id = uuid.uuid4()
    new_teacher = Teacher(
        id=id,
        name=teacher.name,
        age=teacher.age,
        course=teacher.course
    )
    teachers_db.append(new_teacher)
    return new_teacher


@router.get("/", response_model=List[Teacher])
def get_all_teachers():
    return teachers_db