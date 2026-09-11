from fastapi import APIRouter
from Controller.StudentController import (
    CreateStudent,
    GetStudents,
    UpdateStudent as UpdateStudentController,
    DeleteStudent as DeleteStudentController,
)
from Model.StudentModel import StudentStructure
from Model.UpdateModel import updateStructure

router = APIRouter()

@router.post("/createStudent")
def create(student:StudentStructure):
    return CreateStudent(student)

@router.get("/allstudent")
def GetStudent():
    return GetStudents()

@router.put("/edit/{roll}")
def UpdateStudent(roll:int,student:updateStructure):
    return UpdateStudentController(roll, student)

@router.delete("/delete/{roll}")
def DeleteStudent(roll:int):
    return DeleteStudentController(roll)