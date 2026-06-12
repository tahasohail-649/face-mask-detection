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
face-mask-detector/
│
├── train.py # Model training script

├── detect.py # Real-time detection script

├── mask_detector.h5 # Trained model (99.87% accuracy)

├── requirements.txt # Python dependencies

├── README.md # Project documentation

│
├── Train/ # Training images

│ ├── WithMask/ # Mask images (~6000)

│ └── WithoutMask/ # No mask images (~6000)

│
├── Test/ # Testing images

│ ├── WithMask/

│ └── WithoutMask/
│
└── Validation/ # Validation images

├── WithMask/

└── WithoutMask/
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

**1.Environment**
<img width="239" height="69" alt="image" src="https://github.com/user-attachments/assets/756dad5b-7a42-4a57-9753-da6117905237" />

**2.Activate virtual environment**
Windows (PowerShell):
<img width="250" height="76" alt="image" src="https://github.com/user-attachments/assets/cbe5e22d-cb8f-4739-9d7a-2ffffb9c1a13" />
Windows (cmd):
<img width="289" height="79" alt="image" src="https://github.com/user-attachments/assets/c63a62c5-940f-4bf5-867e-e80fe2bf167c" />

**3.Install dependencies**
<img width="235" height="79" alt="image" src="https://github.com/user-attachments/assets/73021f10-e172-439a-8e67-d3aef5b6fe39" />

**4.Run real-time detection**
<img width="211" height="78" alt="image" src="https://github.com/user-attachments/assets/316583aa-e840-48a3-b24b-a6c56203f6ef" />









## Results

| Metric | Value |
|--------|-------|
| Training Accuracy | **99.87%** |
| Validation Accuracy | **99.75%** |
| Loss | 0.0153 |

---

## How to Run

### 1. Clone the repository

##  **Author**

**Taha Sohail**  
BS Computer Science (2022-2026)  
Hazara University, Mansehra  

[GitHub](https://github.com/tahasohail-649) | [LinkedIn](https://linkedin.com/in/taha-sohail-756225318) | [Email](mailto:tahasohail649@gmail.com)

## License

For academic use only. Not licensed for commercial deployment.


