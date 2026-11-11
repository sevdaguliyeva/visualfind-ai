
# VisualFind AI

An offline AI-powered application for finding objects in uploaded images.

## Features

- Upload up to 10 images (JPG, JPEG, PNG).
- Search for objects using English text queries.
- Display matching images in a results gallery.
- Show "No matches found." when no objects are detected.
- Run locally without an internet connection after setup.

## Technologies

- Python
- Streamlit
- PyTorch
- Hugging Face Transformers
- OWL-ViT (`google/owlvit-base-patch32`)
- Pillow

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/sevdaguliyeva/visualfind-ai.git
cd visualfind-ai
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Download the AI model

An internet connection is required for this step.

```bash
python download_model.py
```

The model will be saved locally in `models/owlvit-base-patch32/`.

### 5. Run the application

```bash
python -m streamlit run app.py
```

Open `http://localhost:8501` in your browser.

After downloading the model and installing dependencies, the application can run offline.

## How It Works

1. The user uploads up to 10 images.
2. The user enters an English object name.
3. OWL-ViT analyzes the actual visual content of each image.
4. Images containing detected matches are displayed.
5. If no matches are detected, the application displays "No matches found."

The application does not use filenames, manually assigned tags, hard-coded results, or external AI APIs to determine matches.

## Model Limitations

OWL-ViT may miss objects that are very small, partially hidden, blurry, or photographed from unusual angles.

Detection results depend on the model's confidence threshold and may include false positives or missed objects.

## Demo

A one-minute screen recording demonstrating image upload, object search, and matching results will be included with the submission.
