import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load trained model
model = load_model("models/camera_cnn/trained_model/model.h5")

# Load Haar cascade
face_detector = cv2.CascadeClassifier("utils/haarcascade_frontalface_default.xml")

# Emotion labels
EMOTIONS = ["angry", "disgust", "fear", "happy", "sad", "surprise", "neutral"]

def detect_emotion_from_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        roi = gray[y:y + h, x:x + w]
        roi = cv2.resize(roi, (48, 48))
        roi = roi.astype("float") / 255.0
        roi = np.expand_dims(roi, axis=-1)
        roi = np.expand_dims(roi, axis=0)

        # Predict
        preds = model.predict(roi)[0]
        emotion_index = np.argmax(preds)
        return EMOTIONS[emotion_index]

    return None
