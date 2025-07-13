import cv2

# Load pre-trained Haar Cascade Classifiers dari OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Fungsi utama untuk mendeteksi wajah dan senyuman dari frame video
def detect(gray, frame):
    smile_count = 0

    # Deteksi wajah dalam frame grayscale
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Gambar kotak biru di sekitar wajah
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Potong bagian ROI (Region of Interest) untuk wajah
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Deteksi senyuman di dalam wajah
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)
        smile_count += len(smiles)

        # Gambar kotak merah untuk setiap senyuman
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)

    return frame, smile_count, len(faces)
