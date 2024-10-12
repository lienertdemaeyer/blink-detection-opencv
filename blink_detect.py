from imutils import face_utils
from imutils.video import VideoStream
from scipy.spatial import distance as dist
import cv2
import imutils
import dlib
import time

def eye_aspect_ratio(eye):
    a = dist.euclidean(eye[1], eye[5])
    b = dist.euclidean(eye[2], eye[4])
    c = dist.euclidean(eye[0], eye[3])
    ear = (a + b) / (2 * c)
    return ear

EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 2  # Corrected variable name

counter = 0
total = 0

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

(ls, le) = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
(rs, re) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']

vs = VideoStream(src=0).start()
time.sleep(2.0)

while True:
    image = vs.read()
    image = imutils.resize(image, width=500)
    rects = detector(image, 1)

    for rect in rects:
        shape = predictor(image, rect)
        shape = face_utils.shape_to_np(shape)

        left = shape[ls: le]
        right = shape[rs: re]

        leftEAR = eye_aspect_ratio(left)
        rightEAR = eye_aspect_ratio(right)

        EAR = (leftEAR + rightEAR) / 2

        leftHull = cv2.convexHull(left)
        rightHull = cv2.convexHull(right)

        cv2.drawContours(image, [leftHull], -1, (0, 255, 0), 1)
        cv2.drawContours(image, [rightHull], -1, (0, 255, 0), 1)

        if EAR < EYE_AR_THRESH:
            counter += 1
        else:
            if counter >= EYE_AR_CONSEC_FRAMES:
                total += 1
            counter = 0

        cv2.putText(image, "Blinks: {}".format(total), (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.putText(image, "EAR: {:.2f}".format(EAR), (300, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow('Video', image)
    key = cv2.waitKey(1) & 0xFF  # Changed to waitKey(1)

    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()
