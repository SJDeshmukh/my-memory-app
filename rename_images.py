import os
from PIL import Image

def rename_and_convert_to_jpg(folder_path):
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    supported_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(supported_extensions)]
    files.sort()  # Ensures order is consistent

    temp_folder = os.path.join(folder_path, "temp_conversion")
    os.makedirs(temp_folder, exist_ok=True)

    i = 1
    for filename in files:
        file_path = os.path.join(folder_path, filename)
        try:
            with Image.open(file_path) as img:
                rgb_img = img.convert("RGB")
                new_name = f"image{i}.jpg"
                new_path = os.path.join(temp_folder, new_name)
                rgb_img.save(new_path, "JPEG")
                print(f"Saved: {new_name}")
                i += 1
        except Exception as e:
            print(f"Failed to process {filename}: {e}")
            continue

    # Clean up original folder and move new files in
    for f in files:
        try:
            os.remove(os.path.join(folder_path, f))
        except:
            pass

    for f in os.listdir(temp_folder):
        os.rename(os.path.join(temp_folder, f), os.path.join(folder_path, f))

    os.rmdir(temp_folder)

    print("All images converted and renamed as image1.jpg, image2.jpg, ...")

# Example usage
rename_and_convert_to_jpg("/home/sudhanshu/Documents/personal_projects/Website_to_celebrate/images")
