# Real-Time Object Appearance & Disappearance Detection

This project detects when objects go missing or appear in a video in real-time using YOLOv8 and DeepSORT.

## 📦 Features

- Detect new and missing objects
- YOLOv8 + DeepSORT for tracking
- FPS overlay
- Output video and screenshots

##  Getting Started

### Requirements
- Python 3.10
- GPU (optional but recommended)

### Installation
```bash
git clone https://github.com/AgarwalBhavya/samajh_object_tracking.git
cd samajh_object_tracking
pip install -r requirements.txt

###Create and Activate Virtual Environment (Optional but Recommended)
python -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate

###Install Dependencies
pip install -r requirements.txt

###Run the Pipeline
python -m core.main

###Install Dependencies
