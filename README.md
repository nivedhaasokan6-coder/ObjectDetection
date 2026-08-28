# ObjectDetection
# 🧠 AI Object Detection

An AI-powered object detection web application built with **Python, Streamlit, and Hugging Face Transformers**. The application allows users to upload an image and automatically identifies objects present in the image.

## 🚀 Features

* 📷 Upload JPG, JPEG, and PNG images
* 🧠 Detect objects using the DETR model
* 🎯 Display detected object names
* 📊 Show confidence scores for detected objects
* 💻 Simple and user-friendly Streamlit interface

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Hugging Face Transformers**
* **PyTorch**
* **Torchvision**
* **Pillow**
* **timm**
* **DETR (DEtection TRansformer)**

## 📂 Project Structure

```text
Object-Detection/
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

Clone the repository and open the project folder.

Install the required libraries:

```bash
py -m pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application using:

```bash
py -m streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## 🔍 How It Works

1. Open the Object Detection web application.
2. Upload an image.
3. Click **Detect Objects**.
4. The DETR model analyzes the image.
5. The application displays the detected objects and their confidence scores.

## 🤖 Model

This project uses the **DETR (DEtection TRansformer)** model:

`facebook/detr-resnet-50`

DETR is a transformer-based computer vision model designed for object detection.

## 📌 Note

The model is downloaded automatically the first time the application is run. Internet access is required during the initial model download.

