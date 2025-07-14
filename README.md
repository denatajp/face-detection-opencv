## Face & Smile Detection System
A real-time face and smile detection web application using OpenCV and Flask. Detects faces and smiles through your webcam and displays statistics in an elegant dashboard.

https://denatajp.github.io/face-detection-opencv

### Key Features
- 🎭 Real-time face detection with blue bounding boxes
- 😊 Smile detection within faces with pink highlights
- 📊 Live statistics dashboard (face count, smile count, detection time)
- 🚀 One-click start/stop detection
- 🌙 Dark mode UI with elegant gradients
- 📱 Fully responsive design

### Technology Stack
Frontend:
    HTML5, CSS3 (Flexbox, Grid)
    Vanilla JavaScript
    Font Awesome Icons
Backend:
    Python 3
    Flask (Web framework)
    OpenCV (Computer vision)
    Haar Cascade classifiers

### Installation & Setup
1. Clone the repository:
```bash
git clone https://github.com/denatajp/face-detection-opencv.git
cd face-detection-opencv
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Access the application at:
http://localhost:5000


### Project Structure
```text
├── app.py               # Main Flask application
├── smileDetection.py    # Face and smile detection logic
├── templates/
│   └── index.html       # Main HTML template
├── static/
│   └── style.css        # Custom styles
├── requirements.txt     # Python dependencies
└── README.md            # This file
```
