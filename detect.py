import cv2
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("mask_detector.h5")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Camera open nahi ho rahi")
    exit()

print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(80, 80))
    
    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        if face.size == 0:
            continue
        face = cv2.resize(face, (100, 100))
        face = np.expand_dims(face, axis=0) / 255.0
        
        pred = model.predict(face, verbose=0)[0][0]
        threshold = 0.65
        
        # Labels SWAPPED - ab sahi hoga
        if pred > threshold:
            label = "No Mask"   # 1 pe No Mask
            color = (0, 0, 255) # Red
        else:
            label = "Mask"      # 0 pe Mask
            color = (0, 255, 0) # Green
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    
    cv2.imshow("Face Mask Detector", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()