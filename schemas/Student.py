# Schemas help to serialize and also convert mongodb format json our UI needed json

def studentEntity(db_student) -> dict:
    return {
        "id": str(db_student["_id"]),
        "name": db_student["student_name"],
        "email": db_student["student_email"],
        "phone": db_student["student_phone"],
    }


def studentListEntity(db_student_list) -> list:
    student_list_entity = []

    for student in db_student_list:
        student_list_entity.append(studentEntity(student))
    
    return student_list_entity