from Model.StudentModel import StudentStructure
from Model.UpdateModel import updateStructure
from Database.databaseconnection import collection


def CreateStudent(student:StudentStructure):
    student_info = {
        "roll": student.roll,
        "name": student.name,
        "age": student.age
    }

    collection.insert_one(student_info)
    return {"message":"student created"}


def GetStudents():
    return list(collection.find({}, {"_id": 0}))

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
def UpdateStudent(roll: int, student: updateStructure):
    update_data = {}

    if student.name is not None:
        update_data["name"] = student.name

    if student.age is not None:
        update_data["age"] = student.age

    if not update_data:
        return {"message": "No student fields to update"}

    result = collection.update_one(
        {"roll": roll},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        return {"message": "Student not found"}

    return {"message":"student Updated"}


def DeleteStudent(roll: int):
    result = collection.delete_one({"roll": roll})

    if result.deleted_count == 0:
        return {"message": "Student not found"}

    return {"message":"Student Deleted"}