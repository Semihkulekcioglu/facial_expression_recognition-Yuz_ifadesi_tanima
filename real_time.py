import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Duygu sınıfları
emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Model ve yüz dedektörü yükleme
model = load_model('emotion_model.h5')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def preprocess_face(face_img):
    # Yüz görüntüsünü model için hazırlama
    face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
    face_img = cv2.resize(face_img, (48, 48))
    face_img = np.expand_dims(face_img, axis=0)
    face_img = np.expand_dims(face_img, axis=-1)
    face_img = face_img / 255.0
    return face_img

def main():
    # Kamera başlat
    cap = cv2.VideoCapture(0)
    
    while True:
        # Kameradan görüntü al
        ret, frame = cap.read()
        if not ret:
            break
            
        # Görüntüyü gri tonlamaya çevir
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Yüzleri tespit et
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        for (x, y, w, h) in faces:
            # Yüz bölgesini kes
            face_img = frame[y:y+h, x:x+w]
            
            # Yüz görüntüsünü işle
            processed_face = preprocess_face(face_img)
            
            # Tahmin yap
            predictions = model.predict(processed_face)
            emotion_idx = np.argmax(predictions)
            emotion = emotions[emotion_idx]
            confidence = predictions[0][emotion_idx]
            
            # Sonuçları görüntü üzerine yaz
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f"{emotion}: {confidence:.2f}", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        # Sonucu göster
        cv2.imshow('Real-time Emotion Detection', frame)
        
        # 'q' tuşuna basılırsa çık
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Temizlik
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main() 