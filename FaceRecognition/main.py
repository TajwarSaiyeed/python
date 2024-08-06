import numpy
import face_recognition
import csv
import cv2
import os
from datetime import datetime

video_capture = cv2.VideoCapture(0)
folder =os.path.dirname(os.path.abspath(__file__))

# Load Known faces
mr_robot_face = face_recognition.load_image_file(f"{folder}/faces/mr_robot.jpg")
mr_robot_encoding = face_recognition.face_encodings(mr_robot_face)[0]

shiekh_ahmedullah = face_recognition.load_image_file(f"{folder}/faces/Sheikh_Ahmadullah.jpg")
shiekh_ahmedullah_encoding = face_recognition.face_encodings(shiekh_ahmedullah)[0]

known_face_encodings = [mr_robot_encoding,shiekh_ahmedullah_encoding]
known_face_names = ["Mr. Robot",    "Sheikh Ahmedullah"]

# List of expected students
students = known_face_names.copy()

face_locations = []
face_encodings = []

# Get the current date and time
now = datetime.now()
current_date = now.strftime("%d-%m-%Y")

f = open(f"{current_date}.csv", "w+", newline="")
ln_writer = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = numpy.argmin(face_distance)

        if (matches[best_match_index]):
            name = known_face_names[best_match_index]
            print(name)
            ln_writer.writerow([name, current_date, now.strftime("%H:%M:%S")])
            students.remove(name)

        cv2.imshow("Attendace", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    if len(students) == 0:
        break

f.close()

video_capture.release()

cv2.destroyAllWindows()


