# Real-Time Face Mask Detection

Real-time face mask detection using **MobileNetV2** and **OpenCV**.  
Trained on 12,000+ images with **99.87% accuracy**.

---

## Features

- 🟢 Real-time face mask detection via webcam
- 🟢 Green box = **Mask** | 🔴 Red box = **No Mask**
- 🟢 Works with beard, glasses, and different lighting
- 🟢 Single face box (no duplicates)

---
## Project Structure
```
face-mask-detector/
│
├── train.py # Model training script (MobileNetV2)
├── detect.py # Real-time detection script (webcam)
├── mask_detector.h5 # Trained model (99.87% accuracy)
├── requirements.txt # Python dependencies
├── README.md # Project documentation
│
├── Train/ # Training dataset
│ ├── WithMask/ # Mask images (~6000)
│ │ └── *.jpg, *.png
│ └── WithoutMask/ # No mask images (~6000)
│ └── *.jpg, *.png
│
├── Test/ # Testing dataset
│ ├── WithMask/
│ │ └── *.jpg, *.png
│ └── WithoutMask/
│ └── *.jpg, *.png
│
└── Validation/ # Validation dataset
├── WithMask/
│ └── *.jpg, *.png
└── WithoutMask/
└── *.jpg, *.png
```

---
## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.12 | Programming language |
| TensorFlow / Keras | Deep learning model |
| MobileNetV2 | Pre-trained CNN (transfer learning) |
| OpenCV | Face detection + webcam integration |
| scikit-learn | Train-test split |

---

## Dataset

- **Source:** Kaggle – Face Mask 12k Images Dataset (Ashish Jangra)
- **Images:** 12,000+
- **Classes:** With Mask / Without Mask
---

## Setup

### 1.Environment
```bash
python -m venv mask_env
```

### 2.Activate virtual environment
```bash
mask_env\Scripts\Activate.ps1
```

### 3.Install dependencies
```bash
pip install -r requirements.txt
```

### 4.Run real-time detection
```bash
python detect.py
```
---
## Results

| Metric | Value |
|--------|-------|
| Training Accuracy | **99.87%** |
| Validation Accuracy | **99.75%** |
| Loss | 0.0153 |

---

## Team

| Name | Role |
|------|------|
| Taha Sohail| 



**Institution:** Department of Computer Science, Hazara University Mansehra  


---

## License

For academic use only. Not licensed for commercial deployment.


