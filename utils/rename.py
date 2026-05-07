import os
import csv
 
def rename_and_save(image_folder, prefix, label, start_index=1, digits=6):
    """
    Rename images in the specified folder and prepare data for CSV output.

    Args:
    - image_folder (str): The folder containing the images to rename.
    - prefix (str): Prefix for the new filenames.
    - label (str): Class label to associate with these images.
    - start_index (int): Starting index for numbering.
    - digits (int): Minimum digits for zero-padded numbering.

    Returns:
    - list: A list of [filepath, class] pairs for saving to a CSV.
    """
    image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    if not image_files:
        print(f"No images found in {image_folder}.")
        return []
    
    data = []
    for i, filename in enumerate(image_files, start=start_index):
        file_extension = os.path.splitext(filename)[1].lower()  # Normalize extension to lowercase
        new_filename = f"{prefix}_{i:0{digits}d}{file_extension}"  # Create new filename with leading zeros
        old_filepath = os.path.join(image_folder, filename)
        new_filepath = os.path.join(image_folder, new_filename)

        try:
            os.rename(old_filepath, new_filepath)  # Rename the file
            data.append([new_filepath, label])  # Add the new file path and class label to the data list
        except Exception as e:
            print(f"Error renaming {old_filepath} to {new_filepath}: {e}")
    
    return data

def save_to_csv(data, output_csv):
    """
    Save image data to a CSV file.

    Args:
    - data (list): List of [filepath, class] pairs.
    - output_csv (str): Path to the output CSV file.
    """
    try:
        with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['filepath', 'class'])  # Write header
            writer.writerows(data)  # Write data
        print(f"Data successfully saved to {output_csv}")
    except Exception as e:
        print(f"Error saving data to {output_csv}: {e}")

# Set your folders
real_folder = r'C:\Users\HUAWEI\Desktop\Graduation project\Face-detection\real'
fake_folder = r'C:\Users\HUAWEI\Desktop\Graduation project\Face-detection\Fake'

# Rename files and collect data
real_data = rename_and_save(real_folder, 'r', 'real', start_index=1, digits=6)  # Handles up to 999,999
fake_data = rename_and_save(fake_folder, 'f', 'fake', start_index=1, digits=6)

# Combine data from both folders
all_data = real_data + fake_data

# Save to CSV
output_csv = 'image_labels_2.csv'
save_to_csv(all_data, output_csv)

print(f"Renaming complete and data saved to {output_csv}")