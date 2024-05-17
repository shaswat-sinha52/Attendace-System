## Face Recognition Attendance System

This Python script utilizes face recognition to automate attendance marking. 

### Features

* Recognizes faces using the Face Recognition library.
* Marks attendance of known individuals in a CSV file.
* Alerts for unrecognized faces.
* Announces names of recognized people with text-to-speech functionality.

### Requirements

* Python 3.x
* OpenCV library (https://pypi.org/project/opencv-python/)
* Face Recognition library (https://pypi.org/project/face-recognition/)
* Numpy library (https://pypi.org/project/numpy/)
* Pyttsx3 library (https://pypi.org/project/pyttsx3/)

### Usage

1. Save known faces in the `faces` folder with filenames matching the expected names (e.g., `shaswat.jpeg` for "Shaswat").
2. Update the `known_face_names` and `known_face_encodings` lists in the script with your desired names and corresponding encodings (you can generate encodings using the script itself).
3. Run the script (`python attendance_system.py`).

**Note:** This script is a basic example and might require adjustments based on your specific setup.

### Contributing

We welcome contributions to improve this project. Feel free to submit pull requests with enhancements or bug fixes.


