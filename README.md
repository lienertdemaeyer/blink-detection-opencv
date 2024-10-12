# Blink Detection Project

This project is designed to detect eye blinks using a webcam in real-time. The blink detection algorithm is based on computing the Eye Aspect Ratio (EAR) using facial landmarks, which is then used to identify when a blink occurs.

## Features
- Real-time detection of eye blinks.
- Tracks blink count and displays it on the video feed.
- Utilizes the dlib library for facial landmark detection and OpenCV for video streaming.

## Requirements
- Python 3.10 or higher
- `dlib` for face detection and facial landmark prediction
- `opencv-python` for video processing
- `scipy` for distance calculations
- `imutils` for easier image processing functions

## Installation

### Step 1: Set up a Conda environment with Python 3.10

If you are using Conda, create a new environment with Python 3.10:

```bash
conda create --name blink-detect python=3.10
conda activate blink-detect
