import os
import cv2
import face_recognition
import pickle
import numpy as np

def train_model():
    print("Starting training process...")
    
    # Find the student folder
    student_name = None
    student_folder = None
    
    for item in os.listdir('.'):
        if os.path.isdir(item) and item.startswith('img_'):
            student_folder = item
            student_name = item.replace('img_', '')
            break
            
    if not student_folder:
        print("Error: No folder starting with 'img_' found.")
        print("Please create a folder named 'img_<yourname>' and put your photos in it.")
        return

    print(f"Found folder for student: {student_name}")
    
    known_encodings = []
    
    # Process images in the folder
    image_files = [f for f in os.listdir(student_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not image_files:
        print(f"Error: No images found in {student_folder}")
        return
        
    print(f"Processing {len(image_files)} images...")
    
    for img_file in image_files:
        img_path = os.path.join(student_folder, img_file)
        print(f"Processing {img_file}...")
        
        # Load image
        image = face_recognition.load_image_file(img_path)
        
        # Detect faces and get encodings
        # We assume there's only one person (the student) in the training photos
        encodings = face_recognition.face_encodings(image)
        
        if len(encodings) > 0:
            known_encodings.append(encodings[0])
            print(f"  - Face detected and encoded.")
        else:
            print(f"  - No face detected in {img_file}. Skipping.")
            
    if not known_encodings:
        print("Error: No valid face encodings could be generated from the images.")
        return
        
    # Average the encodings to create a stable profile
    # Each encoding is a 128-dimensional vector
    final_encoding = np.mean(known_encodings, axis=0)
    
    # Save the data
    data = {
        "name": student_name,
        "encoding": final_encoding
    }
    
    with open("encodings.pkl", "wb") as f:
        pickle.dump(data, f)
        
    print(f"\nTraining complete! Model saved for {student_name}.")
    print("You can now run test.py to test the recognition.")

if __name__ == "__main__":
    train_model()

