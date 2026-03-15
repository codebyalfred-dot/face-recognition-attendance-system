import face_recognition
import cv2
import numpy as np

def encode_face(image_bytes):

    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    encodings = face_recognition.face_encodings(rgb)

    if len(encodings) > 0:
        return encodings[0].tolist()

    return None


def compare_faces(known, unknown):

    known = np.array(known)
    unknown = np.array(unknown)

    result = face_recognition.compare_faces([known], unknown)

    return result[0]