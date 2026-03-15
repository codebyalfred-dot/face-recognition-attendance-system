FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libgl1 \
    libglib2.0-0

COPY backend/ /app

RUN pip install --no-cache-dir fastapi uvicorn opencv-python face-recognition numpy sqlalchemy python-multipart

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]