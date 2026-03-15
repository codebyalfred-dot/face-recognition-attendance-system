# Face Recognition Attendance System

A web-based attendance system that uses **face recognition** to automatically mark student attendance.

The system captures images from a webcam, compares faces with registered students, and records attendance with date and time.

---

## Features

- Register student face using webcam
- Face recognition based attendance marking
- Attendance dashboard
- FastAPI backend API
- SQLite database
- Docker support
- Browser-based camera interface

---

## Tech Stack

- Python
- FastAPI
- OpenCV
- face_recognition library
- SQLite
- HTML / JavaScript
- Docker

---

## Project Structure

face-recognition-attendance-system
│
├── backend
│ ├── main.py
│ ├── models.py
│ ├── database.py
│ └── face_utils.py
│
├── frontend
│ ├── register.html
│ ├── attendance.html
│ └── dashboard.html
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore

---

## Installation

### 1. Clone the repository

git clone https://github.com/codebyalfred-dot/face-recognition-attendance-system.git

cd face-recognition-attendance-system

---

### 2. Run with Docker

Build the image: docker build -t attendance-system

Run the container: docker run -p 8000:8000 attendance-system

---

### 3. Open API documentation

http://localhost:8000/docs

---

## Pages

| Page | Description |
|-----|-----|
| register.html | Register student face |
| attendance.html | Mark attendance |
| dashboard.html | View attendance records |

---

## Future Improvements

- Teacher login system
- Prevent duplicate attendance
- Export attendance to CSV
- Real-time face detection
- Mobile support

---

## Author

Alfred Griffin  
Computer Engineering Student