from fastapi import APIRouter
import uuid
from typing import List
from models.student import Student, StudentCreate
from database import students_db

router = APIRouter(prefix="/students")


@router.post("/", response_model=Student)
def create_student(student: StudentCreate):
    id = uuid.uuid4()
    new_student = Student(
        id=id,
        name=student.name,
        age=student.age,
        course=student.course
    )
    students_db.append(new_student)


@router.get("/", response_model=List[Student])
def get_all_students():
    return students_db