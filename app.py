from flask import Flask, render_template, Response, jsonify
import cv2
import time
from smileDetection import detect  # fungsi deteksi wajah & senyuman

app = Flask(__name__)

# Inisialisasi webcam (0 = default camera)
video_capture = cv2.VideoCapture(0)

# Variabel global untuk menyimpan statistik deteksi
detection_stats = {
    "face_count": 0,
    "smile_count": 0,
    "start_time": time.time()
}

# Fungsi generator untuk mengirimkan frame video secara real-time
def generate_frames():
    while True:
        success, frame = video_capture.read()
        if not success:
            break

        # Konversi ke grayscale untuk proses deteksi
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Jalankan proses deteksi wajah dan senyuman
        frame, smile_count, face_count = detect(gray, frame)

        # Simpan data deteksi ke dalam variabel global
        detection_stats["face_count"] = face_count
        detection_stats["smile_count"] = smile_count

        # Encode frame ke format JPEG sebelum dikirimkan ke frontend
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Kirim frame dalam format streaming multipart
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# Endpoint untuk mengambil statistik deteksi secara real-time
@app.route('/get_stats')
def get_stats():
    elapsed_time = int(time.time() - detection_stats["start_time"])
    return jsonify({
        **detection_stats,
        "elapsed_time": elapsed_time
    })


# Endpoint utama (render halaman index.html)
@app.route('/')
def index():
    return render_template('index.html')


# Endpoint untuk video streaming dari kamera
@app.route('/video_feed')
def video_feed():
    try:
        return Response(generate_frames(),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
    except Exception as e:
        print("Error in video feed:", str(e))
        return str(e), 500


# Jalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)
