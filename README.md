
# 👁️ Simple Face Detection using Haar Cascade

This is a simple Python script that performs face detection in real-time using OpenCV and Haar Cascade Classifier.

## 📷 Features

- Detect faces from a live webcam feed
- Draw bounding boxes around detected faces
- Lightweight and easy to run on most systems

## 🧠 Tech Stack

- **Language**: Python
- **Library**: OpenCV (cv2)
- **Model**: Haar Cascade (pre-trained by OpenCV)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/face-detection-haarcascade.git
cd face-detection-haarcascade
```

### 2. Install Requirements

```bash
pip install opencv-python
```

### 3. Run the Script

```bash
python detect_faces.py
```

The webcam window will open, and faces will be detected in real time.

## 📁 Files

```
face-detection-haarcascade/
├── haarcascade_frontalface_default.xml
├── detect_faces.py
└── README.md
```

## 📝 How it Works

1. The script loads the Haar Cascade classifier XML file.
2. Captures video from your webcam using OpenCV.
3. Converts each frame to grayscale.
4. Applies the Haar Cascade model to detect faces.
5. Draws rectangles around the detected faces.

## 📧 Contact

Sanoy Boby  
📫 Email: sanoyboby924@gmail.com  
📱 Phone: +91 6235534401

## 📄 License

This project is licensed under the MIT License.
