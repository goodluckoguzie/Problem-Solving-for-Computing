# Simple Facial Recognition System with YOLO

This project allows you to train a system to recognize your face using your own images and then test it in real-time using your webcam. It uses YOLOv8 for detection and the `face_recognition` library for identification.

## Prerequisites

1.  **Install Python:** Ensure you have Python installed.
2.  **Install Dependencies:** Run the following command in your terminal:

    ```bash
    pip install -r requirements.txt
    ```

    *Note: Installing `face_recognition` might require Visual Studio C++ build tools on Windows (for `dlib`). If you encounter errors, search for "install dlib python windows".*

## Instructions

### Step 1: Prepare Your Images

1.  Create a new folder named `img_<yourname>` in this directory.
    *   Example: If your name is Bisi, create a folder named `img_bisi`.
2.  Take 3-5 clear photos of your face (selfies work well) and put them inside that folder.
    *   Ensure your face is clearly visible.
    *   Supported formats: .jpg, .png, .jpeg

### Step 2: Train the Model

1.  Run the training script:

    ```bash
    python train.py
    ```

2.  The script will look for your folder, detect your face in the images, and learn your features.
3.  When finished, it will save a file named `encodings.pkl` and display a success message.

### Step 3: Test Recognition

1.  Run the testing script:

    ```bash
    python test.py
    ```

2.  The script will download the YOLO model (first time only) and open your webcam.
3.  Point the camera at your face.
    *   If it recognizes you, it will draw a GREEN box and show your name.
    *   If it sees someone else (or doesn't recognize you), it will draw a RED box and show "Unknown".
4.  Press `q` on your keyboard to quit the application.

## Troubleshooting

*   **No folder found:** Make sure your folder starts with `img_` (e.g., `img_john`).
*   **Webcam not opening:** Check if another app is using the camera.
*   **Installation errors:** If `pip install` fails on `dlib` or `face_recognition`, try installing the pre-compiled wheel for dlib first.

