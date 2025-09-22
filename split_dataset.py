import os
import shutil
import random

train_dir = 'dataset/train'
validation_dir = 'dataset/validation'
split_ratio = 0.2  # %20 validation

os.makedirs(validation_dir, exist_ok=True)

for emotion in os.listdir(train_dir):
    emotion_train_dir = os.path.join(train_dir, emotion)
    emotion_val_dir = os.path.join(validation_dir, emotion)
    os.makedirs(emotion_val_dir, exist_ok=True)
    images = os.listdir(emotion_train_dir)
    val_count = int(len(images) * split_ratio)
    val_images = random.sample(images, val_count)
    for img in val_images:
        src = os.path.join(emotion_train_dir, img)
        dst = os.path.join(emotion_val_dir, img)
        shutil.move(src, dst)

print("Bölme işlemi tamamlandı.") 