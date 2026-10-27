<div align="center">

# 🏗️ Crane Signal AI

**Real-time recognition of crane hand signals from live video, using deep learning and TensorFlow Lite.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![TensorFlow Lite](https://img.shields.io/badge/TensorFlow%20Lite-edge%20ready-FF6F00?logo=tensorflow&logoColor=white)
![Model](https://img.shields.io/badge/Model-MoViNet--A2-4285F4)
![Flask](https://img.shields.io/badge/API-Flask-000000?logo=flask&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-2ea44f)

</div>

<!-- TODO: add a demo GIF or screenshot here, e.g. ![Demo](docs/demo.gif) -->

---

## 🔍 Overview

**Crane Signal AI** is a computer-vision system that recognizes **standardized crane hand signals** from a webcam stream or recorded clips. It uses a lightweight [MoViNet](https://arxiv.org/abs/2103.11511) video model trained on labeled gesture data and converted to **TensorFlow Lite** so it can run on edge devices and safety systems.

## 💡 Use cases

| Today | Future possibilities |
|---|---|
| 🦺 **Construction safety monitoring**: flag ambiguous or unsafe signals in real time | 🏗️ **AI-controlled cranes** that respond to recognized hand signals |
| 📹 **Operator assistance**: a second set of eyes in noisy, high-risk sites | 🧠 **Smart surveillance** using existing site camera feeds |
| 🧪 **Dataset labeling**: auto-label crane videos for better training data | 🕹️ **Remote operation** through gesture input |
| | 👓 **AR glasses / helmet HUD** showing detected signals live |

## 🧠 Model

| Component | Details |
|---|---|
| Base model | MoViNet-A2 |
| Input resolution | 224 × 224 |
| Frames per clip | 30 |
| Modes | Offline (clip-based) and streaming (frame-by-frame) |
| Export format | TensorFlow Lite (`.tflite`) |

## ✨ Features

- ✅ Real-time crane gesture classification
- ✅ **Streaming mode**: frame-by-frame inference with memory states
- ✅ **Offline mode**: clip-based inference
- ✅ TensorFlow Lite models for edge deployment
- ✅ Flask web API with live video overlay
- ✅ Dataset augmentation with Albumentations
- ✅ Prediction visualization tools

## 🚀 Quick start

```bash
git clone https://github.com/Emdysuji/CraneSignalAI.git
cd CraneSignalAI

python -m venv .venv
# Windows: .venv\Scripts\activate    |    Linux/macOS: source .venv/bin/activate

pip install -r requirements.txt
```

<!-- TODO: confirm requirements.txt exists in the repo root (it was not in the file list) -->

Run the live **streaming** API (frame-by-frame):

```bash
python API/api_live_stream.py
```

Or the **offline** clip-based API:

```bash
python API/api_live_base.py
```

<!-- TODO: confirm the default port and URL to open, then add it here -->

## 📁 Project structure

```
CraneSignalAI/
├── API/
│   ├── api_live_base.py        # Offline clip-based video API
│   └── api_live_stream.py      # Streaming (frame-by-frame) video API
├── Models/
│   ├── model_3_b30.tflite      # Base (non-streaming) model
│   └── model_3.tflite          # Streaming inference model
├── utils/
│   ├── cut_video_clips.py      # Slice video into short labeled segments
│   └── augment_videos.py       # Run augmentation on the dataset
├── CraneSignalTraining.ipynb   # Full training + export notebook
├── requirements.txt
└── README.md
```

## 🎓 Training your own model

Open `CraneSignalTraining.ipynb` in Jupyter or Google Colab. It covers loading the labeled clips, augmentation, training MoViNet-A2, and exporting the `.tflite` models into `Models/`.

## 🙏 Acknowledgements

- [TensorFlow Model Garden: MoViNet](https://www.kaggle.com/code/minhdunk/movinet-streaming#Convert-to-TF-Lite)
- [Albumentations](https://albumentations.ai) for fast image and video augmentation
- Dataset videos: public crane hand-signal videos on YouTube

## 📄 License

Released under the **MIT License**. See [LICENSE](LICENSE).

## 🧑‍💻 Author

**Michael-David Osuji**, AI Engineer
[LinkedIn](https://www.linkedin.com/in/michael-david-osuji) · [GitHub](https://github.com/Emdysuji)

<div align="center">

⭐ If this project is useful to you, consider starring the repo.

</div>
