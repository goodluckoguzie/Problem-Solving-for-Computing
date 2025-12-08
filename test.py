import cv2
import pickle
import numpy as np
from ultralytics import YOLO
from deepface import DeepFace
from scipy.spatial.distance import cosine

def test_recognition():
    print("Loading facial recognition system...")
    
    # Load saved embeddings
    try:
        with open("encodings.pkl", "rb") as f:
            data = pickle.load(f)
            saved_embedding = data["embedding"]
            student_name = data["name"]
            model_name = data.get("model_name", "VGG-Face")
            print(f"Loaded profile for: {student_name}")
    except FileNotFoundError:
        print("Error: encodings.pkl not found. Please run train.py first.")
        return

    # Initialize YOLO model
    try:
        model = YOLO('yolov8n.pt')
        print("YOLO model loaded.")
    except Exception as e:
        print(f"Error loading YOLO model: {e}")
        return

    # Initialize webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Starting webcam... Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # YOLO detection
        results = model(frame, stream=True, verbose=False)
        
        # Process detections
        for result in results:
            boxes = result.boxes
            for box in boxes:
                # Check if class is 'person' (class 0)
                if int(box.cls[0]) == 0:
                    # Get coordinates
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    
                    # Ensure coordinates are within frame
                    h, w, _ = frame.shape
                    x1, y1 = max(0, x1), max(0, y1)
                    x2, y2 = min(w, x2), min(h, y2)
                    
                    # Extract face/person region
                    face_img = frame[y1:y2, x1:x2]
                    
                    if face_img.size == 0:
                        continue
                        
                    try:
                        # Get embedding for the detected face
                        # enforce_detection=False allows processing even if face is not perfectly clear
                        embedding_objs = DeepFace.represent(img_path = face_img, 
                                                          model_name = model_name, 
                                                          enforce_detection = False)
                        
                        if embedding_objs:
                            current_embedding = embedding_objs[0]["embedding"]
                            
                            # Calculate distance (lower is better match)
                            dist = cosine(saved_embedding, current_embedding)
                            
                            # Threshold for VGG-Face is typically around 0.4 - 0.5
                            threshold = 0.5
                            
                            name = "Unknown"
                            color = (0, 0, 255) # Red
                            
                            if dist < threshold:
                                name = student_name
                                color = (0, 255, 0) # Green
                                
                            # Draw box and label
                            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                            cv2.putText(frame, f"{name} ({dist:.2f})", (x1, y1 - 10), 
                                      cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
                                      
                    except Exception:
                        pass

        # Display result
        cv2.imshow('Facial Recognition (YOLO + DeepFace)', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_recognition()
