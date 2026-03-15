from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine
import models
import face_utils
import datetime
import json

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all websites
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()


@app.post("/register")
async def register_student(
    name: str = Form(...),
    roll: str = Form(...),
    file: UploadFile = File(...)
):

    image = await file.read()

    encoding = face_utils.encode_face(image)

    if encoding is None:
        return {"error": "Face not detected"}

    student = models.Student(
        name=name,
        roll=roll,
        face_encoding=json.dumps(encoding)
    )

    db.add(student)
    db.commit()

    return {"message": "Student registered"}
    

@app.post("/mark_attendance")
async def mark_attendance(file: UploadFile = File(...)):

    image = await file.read()

    unknown = face_utils.encode_face(image)

    students = db.query(models.Student).all()

    for student in students:

        known = json.loads(student.face_encoding)

        if face_utils.compare_faces(known, unknown):

            now = datetime.datetime.now()

            attendance = models.Attendance(
                student_id=student.id,
                date=str(now.date()),
                time=str(now.time()),
                status="Present"
            )

            db.add(attendance)
            db.commit()

            return {"message": f"{student.name} marked present"}

    return {"message": "Face not recognized"}
    

@app.get("/attendance")
def view_attendance():

    records = db.query(models.Attendance).all()

    result = []

    for r in records:
        student = db.query(models.Student).filter(models.Student.id == r.student_id).first()

        result.append({
            "id": r.id,
            "name": student.name,
            "date": r.date,
            "time": r.time,
            "status": r.status
        })

    return result