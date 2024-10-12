# Blink Detection Project


![blinking detection demo](https://github.com/user-attachments/assets/48b7d357-c237-48c8-b12a-9562f638fe7d)

This project implements a real-time blink detection system using a webcam. The detection algorithm is based on calculating the Eye Aspect Ratio (EAR) using facial landmarks to identify when a blink occurs. The application uses `dlib` for facial landmark detection and `OpenCV` for video streaming.

## Features
- Real-time detection of eye blinks with a live video feed.
- Tracks the number of blinks and displays the count on the video feed.
- Utilizes `dlib` for detecting facial landmarks and `OpenCV` for video processing.

## Installation

### Step 1: Set Up a Conda Environment with Python 3.10
To ensure compatibility with the required libraries, it's recommended to use Python 3.10. You can create a Conda environment as follows:
```bash
conda create --name blink-detect python=3.10
```
Activate the newly created environment:
```bash
conda activate blink-detect
```

### Step 2: Install Dependencies
After activating the environment, you can install the necessary dependencies from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```
Alternatively, install the dependencies manually:
```bash
pip install dlib opencv-python scipy imutils
```

### Step 3: Download the Facial Landmark Predictor
The blink detection algorithm relies on dlib's pre-trained facial landmark model. Download the `shape_predictor_68_face_landmarks.dat` model from [this link](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2) and extract it. Once extracted, move the `shape_predictor_68_face_landmarks.dat` file into the same directory as the `blink_detect.py` script.

### Step 4: Run the Blink Detection Script
After setting up everything, you can now run the blink detection script:
```bash
python blink_detect.py
```
The script will start a video feed using your webcam, calculate the Eye Aspect Ratio (EAR) from the facial landmarks, and track your blinks in real time. The blink count and EAR values will be displayed on the video feed.

### Step 5: How to Exit
Press the `q` key at any time to stop the video feed and exit the program.

## Troubleshooting
- **GStreamer Warning**: If you encounter warnings related to GStreamer, you can try forcing OpenCV to use a different backend like DirectShow by modifying the video capture initialization in `blink_detect.py`:
  ```python
  vs = cv2.VideoCapture(0, cv2.CAP_DSHOW)
  ```
- **File Not Found Error**: Ensure that `shape_predictor_68_face_landmarks.dat` is in the correct directory and that the file path is correctly specified in the code.

## License
This project is open source and available under the [MIT License](LICENSE).
