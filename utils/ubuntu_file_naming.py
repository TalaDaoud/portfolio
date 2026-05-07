import os
import pandas as pd

def generate_csv(base_dir, output_csv):
    # Define subdirectories for fake and real images
    fake_dir = os.path.join(base_dir, "image-fake")
    real_dir = os.path.join(base_dir, "image-real")

    # Prepare lists for file paths and labels
    filepaths = []
    labels = []

    # Process fake images
    for filename in os.listdir(fake_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Adjust file extensions as needed
            filepaths.append(os.path.join(fake_dir, filename))
            labels.append('fake')

    # Process real images
    for filename in os.listdir(real_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Adjust file extensions as needed
            filepaths.append(os.path.join(real_dir, filename))
            labels.append('real')

    # Create a DataFrame
    data = pd.DataFrame({
        'filepath': filepaths,
        'class': labels
    })

    # Save to CSV
    data.to_csv(output_csv, index=False)
    print(f"CSV file created successfully: {output_csv}")

'''# Set base directory and output CSV path
base_dir = "/home/motaseam/Desktop/ai_human_face_classifier/data"
output_csv = "/home/motaseam/Desktop/ai_human_face_classifier/data/image_labels_u.csv"

# Generate the CSV
generate_csv(base_dir, output_csv)'''
