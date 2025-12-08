import os
import cv2
import pickle
import numpy as np
from deepface import DeepFace

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
    
    known_embeddings = []
    
    # Process images in the folder
    image_files = [f for f in os.listdir(student_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not image_files:
        print(f"Error: No images found in {student_folder}")
        return
        
    print(f"Processing {len(image_files)} images...")
    
    for img_file in image_files:
        img_path = os.path.join(student_folder, img_file)
        print(f"Processing {img_file}...")
        
        try:
            # Generate embedding using DeepFace
            # We use 'VGG-Face' model by default as it's balanced
            embedding_objs = DeepFace.represent(img_path = img_path, model_name = "VGG-Face", enforce_detection = False)
            
            if len(embedding_objs) > 0:
                # Take the first face found
                embedding = embedding_objs[0]["embedding"]
                known_embeddings.append(embedding)
                print(f"  - Face processed.")
            else:
                print(f"  - No face detected in {img_file}. Skipping.")
        except Exception as e:
            print(f"  - Error processing {img_file}: {e}")
            
    if not known_embeddings:
        print("Error: No valid face embeddings could be generated from the images.")
        return
        
    # Average the embeddings to create a stable profile
    final_embedding = np.mean(known_embeddings, axis=0)
    
    # Save the data
    data = {
        "name": student_name,
        "embedding": final_embedding,
        "model_name": "VGG-Face"
    }
    
    with open("encodings.pkl", "wb") as f:
        pickle.dump(data, f)
        
    print(f"\nTraining complete! Model saved for {student_name}.")
    print("You can now run test.py to test the recognition.")

if __name__ == "__main__":
    train_model()
