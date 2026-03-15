from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    roll = Column(String)
    face_encoding = Column(String)

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    date = Column(String)
    time = Column(String)
    status = Column(String)