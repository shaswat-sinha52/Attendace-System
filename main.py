import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import pyttsx3

engine = pyttsx3.init()
video_capture = cv2.VideoCapture(0)

shaswat_image= face_recognition.load_image_file("faces/shaswat.jpeg")
shaswat_encoding = face_recognition.face_encodings(shaswat_image)[0]

known_face_encodings = [ shaswat_encoding]
known_face_names = [ "Shaswat"]
# listed of expected students
students = known_face_names.copy()

face_locations = []
face_encodings = []

# storing attendance time
now = datetime.now()
current_date = now.strftime("%d-%m-%Y")

f=open(f"{current_date}.csv", "w+", newline="")
lnwriter=csv.writer(f)
while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        name = "Unknown"
        if matches[best_match_index]:
            name = known_face_names[best_match_index]


        cv2.rectangle(frame, (left * 4, top * 4), (right * 4, bottom * 4), (0, 255, 0), 2)

        if name == "Unknown":
            # Play beep sound for a stranger
            engine.say("Stranger detected")
            engine.runAndWait()


        if name in known_face_names:
            cv2.putText(frame,
                        f"{name} Present",
                        (left * 4, top * 4 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0, 255, 0),
                        2)
            engine.say(name)
            engine.runAndWait()
        else:
            cv2.putText(frame,
                        "Stranger detected",
                        (left * 4, top * 4 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0, 0, 255),
                        2)
        if name in students:
            students.remove(name)
            current_time=now.strftime("%d-%m-%Y")
            lnwriter.writerow([name,current_time,name])


    cv2.imshow("Attendance System", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()


