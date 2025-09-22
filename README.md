# Yüz İfadesi Tanıma Projesi | Facial Expression Recognition Project

[English](README_EN.md) | [Türkçe](README.md)

## 📌 Proje Hakkında

Bu proje, derin öğrenme teknikleri kullanarak insan yüzlerindeki duygu durumlarını gerçek zamanlı olarak tespit eden bir yapay zeka sistemidir. Convolutional Neural Network (CNN) mimarisi kullanılarak geliştirilmiş olup, yüksek doğruluk oranıyla 7 farklı duygu durumunu tanıyabilmektedir.

## 🎯 Özellikler

- 7 farklı duygu durumu tanıma:
  - 😊 Mutlu (Happy)
  - 😢 Üzgün (Sad)
  - 😠 Kızgın (Angry)
  - 😮 Şaşkın (Surprise)
  - 😨 Korkmuş (Fear)
  - 🤢 İğrenmiş (Disgust)
  - 😐 Nötr (Neutral)
- Gerçek zamanlı yüz ifadesi tanıma
- Tek görüntü üzerinden yüz ifadesi analizi
- Yüksek doğruluk oranı
- Hızlı işlem süresi

## 🛠️ Kullanılan Teknolojiler

- Python 3.8
- TensorFlow 2.x
- OpenCV
- NumPy
- Pillow
- Keras

## ⚙️ Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/Semihkulekcioglu/facial_expression_recognition-Yuz_ifadesi_tanima.git
cd facial_expression_recognition-Yuz_ifadesi_tanima
```

2. Sanal ortam oluşturun ve aktifleştirin:
```bash
conda create -n yuz_tanima python=3.8
conda activate yuz_tanima
```

3. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

## 🚀 Kullanım

### Model Eğitimi
```bash
python train.py
```
- Eğitim süresi yaklaşık 2-3 saat sürebilir
- Eğitim sonuçları 'emotion_model.h5' olarak kaydedilir
- Eğitim metrikleri terminal üzerinden takip edilebilir

### Gerçek Zamanlı Test
```bash
python real_time.py
```
- Webcam üzerinden gerçek zamanlı tanıma yapar
- Çıkmak için 'q' tuşuna basın

### Tek Görüntü Testi
```bash
python predict.py test_image.jpg
```
- Belirtilen görüntü üzerinde duygu analizi yapar
- Sonuçları görsel olarak gösterir

## 📊 Model Performansı

- Eğitim Doğruluğu: ~90%
- Validasyon Doğruluğu: ~85%
- FPS (Gerçek Zamanlı): ~30fps

## 📁 Proje Yapısı

```
facial_expression_recognition-Yuz_ifadesi_tanima/
│
├── train.py           # Model eğitim scripti
├── predict.py         # Tek görüntü üzerinde tahmin
├── real_time.py       # Gerçek zamanlı tahmin
├── requirements.txt   # Gerekli kütüphaneler
├── dataset/          # Veri seti klasörü
│   ├── train/       # Eğitim verileri
│   └── validation/  # Doğrulama verileri
└── models/          # Eğitilmiş model dosyaları
```

## 🤝 Katkıda Bulunma

1. Bu projeyi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakınız.