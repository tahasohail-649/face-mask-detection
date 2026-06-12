import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.applications import MobileNetV2

# Dataset ka path
dataset_path = "Train"

# Categories (exact folder names)
categories = ["WithMask", "WithoutMask"]

data = []
labels = []

print("Loading images...")
for category in categories:
    path = os.path.join(dataset_path, category)
    label = categories.index(category)
    
    for img_name in os.listdir(path):
        img_path = os.path.join(path, img_name)
        img = cv2.imread(img_path)
        if img is None:
            continue
        img = cv2.resize(img, (100, 100))
        data.append(img)
        labels.append(label)

# Convert to numpy arrays
data = np.array(data, dtype="float32") / 255.0
labels = np.array(labels)

print(f"Total images loaded: {len(data)}")

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

print(f"Training images: {len(x_train)}")
print(f"Testing images: {len(x_test)}")

# Model banate hain
print("Building model...")
base_model = MobileNetV2(input_shape=(100, 100, 3), include_top=False, weights='imagenet')
base_model.trainable = False

model = keras.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Training
print("Training model... (ye 15-20 minutes lagega)")
model.fit(x_train, y_train, epochs=15, validation_data=(x_test, y_test), batch_size=32)

# Model save karo
model.save("mask_detector.h5")
print("Model saved as mask_detector.h5")