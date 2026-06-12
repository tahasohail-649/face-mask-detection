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

## Results

| Metric | Value |
|--------|-------|
| Training Accuracy | **99.87%** |
| Validation Accuracy | **99.75%** |
| Loss | 0.0153 |

---

## How to Run

### 1. Clone the repository
```bash
## 👨‍💻 Author

**Taha Sohail**  
BS Computer Science (2022-2026)  
Hazara University, Mansehra  

[GitHub](https://github.com/tahasohail-649) | [LinkedIn](https://linkedin.com/in/taha-sohail-756225318) | [Email](mailto:tahasohail649@gmail.com)

## License

For academic use only. Not licensed for commercial deployment.


