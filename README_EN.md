# Facial Expression Recognition Project

[English](README_EN.md) | [Türkçe](README.md)

## 📌 About The Project

This project is an artificial intelligence system that detects human facial expressions in real-time using deep learning techniques. Developed using Convolutional Neural Network (CNN) architecture, it can recognize 7 different emotional states with high accuracy.

## 🎯 Features

- Recognition of 7 different emotional states:
  - 😊 Happy
  - 😢 Sad
  - 😠 Angry
  - 😮 Surprise
  - 😨 Fear
  - 🤢 Disgust
  - 😐 Neutral
- Real-time facial expression recognition
- Single image facial expression analysis
- High accuracy rate
- Fast processing time

<img width="450" height="450" alt="Output_1" src="https://github.com/user-attachments/assets/01bd669b-5b45-4f03-8b11-cc57b782e990" />

## 🛠️ Technologies Used

- Python 3.8
- TensorFlow 2.x
- OpenCV
- NumPy
- Pillow
- Keras

## ⚙️ Installation

1. Clone the project:
```bash
git clone https://github.com/Semihkulekcioglu/facial_expression_recognition-Yuz_ifadesi_tanima.git
cd facial_expression_recognition-Yuz_ifadesi_tanima
```

2. Create and activate virtual environment:
```bash
conda create -n face_recognition python=3.8
conda activate face_recognition
```

3. Install required libraries:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Model Training
```bash
python train.py
```
- Training may take a few hours
- Training results are saved as 'emotion_model.h5'
- Training metrics can be monitored through terminal

### Real-Time Testing
```bash
python real_time.py
```
- Performs real-time recognition through webcam
- Press 'q' to exit

### Single Image Testing
```bash
python predict.py test_image.jpg
```
- Performs emotion analysis on the specified image
- Shows results visually

## 📊 Model Performance

- Training Accuracy: ~90%
- Validation Accuracy: ~85%
- FPS (Real-time): ~30fps

## 📁 Project Structure

```
facial_expression_recognition-Yuz_ifadesi_tanima/
│
├── train.py           # Model training script
├── predict.py         # Single image prediction
├── real_time.py       # Real-time prediction
├── requirements.txt   # Required libraries
├── dataset/          # Dataset directory
│   ├── train/       # Training data
│   └── validation/  # Validation data
└── models/          # Trained model files
```

## 🤝 Contributing

1. Fork this project
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) file for details.
