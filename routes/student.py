from fastapi import APIRouter
from models.Student import Student
from config.database import connection
from schemas.Student import studentEntity, studentListEntity
from bson import ObjectId

student_router = APIRouter()

# Get all students
@student_router.get('/students')
async def get_all_students():
    return studentListEntity(connection.local.student.find())

# Get one student with matching ID
@student_router.get(".=/students/{studentId}")
async def find_student_by_id(studentId):
    return studentEntity(connection.local.find_one({"_id": ObjectId(studentId)}))

# Add a student
@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return studentListEntity(connection.local.student.find())


# Update a student
@student_router.put('/students/{studentId}')
async def update_student(studentId, student: Student):
    connection.local.student.find_one_and_update(
       
        {"_id": ObjectId(studentId)},
        {"$set": dict(student)}
    
    )
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))

#Delete a student
@student_router.delete('/students/{studentId}')
async def delete_student(studentId):
    return studentEntity(connection.local.student.find_one_and_delete({"_id": ObjectId(studentId)}))