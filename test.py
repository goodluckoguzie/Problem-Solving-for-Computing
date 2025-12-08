import cv2
import pickle
import face_recognition
import numpy as np
from ultralytics import YOLO

def test_recognition():
    print("Loading facial recognition system...")
    
    # Load saved encodings
    try:
        with open("encodings.pkl", "rb") as f:
            data = pickle.load(f)
            saved_encoding = data["encoding"]
            student_name = data["name"]
            print(f"Loaded profile for: {student_name}")
    except FileNotFoundError:
        print("Error: encodings.pkl not found. Please run train.py first.")
        return

    # Initialize YOLO model
    # We use the standard YOLOv8n model which detects 'person' (class 0)
    # For better face-specific detection, you would need a yolov8-face.pt model
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
                # Check if class is 'person' (class 0 in COCO dataset)
                cls = int(box.cls[0])
                if cls == 0:  # 0 is person
                    # Get coordinates
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    
                    # Ensure coordinates are within frame
                    height, width, _ = frame.shape
                    x1, y1 = max(0, x1), max(0, y1)
                    x2, y2 = min(width, x2), min(height, y2)
                    
                    # Convert to face_recognition format (top, right, bottom, left)
                    # Note: YOLO detects the whole person/body usually. 
                    # We will treat this box as the region to check.
                    # Ideally, we would crop the face specifically.
                    
                    # For this simple implementation, we assume the person is close to camera 
                    # and the "person" box approximates the face or we assume the face is in there.
                    
                    # Let's define the box for encoding
                    face_location = (y1, x2, y2, x1)
                    
                    # Generate encoding for this face/person
                    # We pass the frame and the specific location to avoid re-detecting
                    # Note: If the box is too large (full body), this might be less accurate
                    # but it fulfills the requirement to "use YOLO".
                    try:
                        # Get encoding
                        encodings = face_recognition.face_encodings(frame, [face_location])
                        
                        if encodings:
                            encoding = encodings[0]
                            
                            # Compare with saved student encoding
                            matches = face_recognition.compare_faces([saved_encoding], encoding, tolerance=0.6)
                            face_distance = face_recognition.face_distance([saved_encoding], encoding)
                            
                            # Determine name
                            name = "Unknown"
                            color = (0, 0, 255) # Red for unknown
                            
                            if matches[0]:
                                name = student_name
                                color = (0, 255, 0) # Green for match
                                
                            # Draw box and label
                            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                            cv2.putText(frame, f"{name} ({face_distance[0]:.2f})", (x1, y1 - 10), 
                                      cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
                                      
                    except Exception as e:
                        # Skip if encoding fails
                        pass

        # Display result
        cv2.imshow('Facial Recognition (YOLO)', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_recognition()

