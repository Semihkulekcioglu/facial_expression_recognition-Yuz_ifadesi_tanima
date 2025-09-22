# Yüz İfadesi Tanıma Projesi

Bu proje, derin öğrenme kullanarak yüz ifadelerini tanıyan bir sistem geliştirmeyi amaçlamaktadır.

## Özellikler

- 7 farklı duygu durumu tanıma (Mutlu, Üzgün, Kızgın, Şaşkın, Korkmuş, İğrenmiş, Nötr)
- Gerçek zamanlı yüz ifadesi tanıma
- Görüntü üzerinden yüz ifadesi tanıma

## Gereksinimler

```
tensorflow
opencv-python
numpy
pillow
```

## Kurulum

1. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

2. Modeli eğitin:
```bash
python train.py
```

3. Gerçek zamanlı test için:
```bash
python real_time.py
```

## Kullanım

- Modeli eğitmek için `train.py`
- Tek bir görüntü üzerinde test için `predict.py`
- Gerçek zamanlı test için `real_time.py`

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır.
