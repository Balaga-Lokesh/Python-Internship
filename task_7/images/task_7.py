import os
from PIL import Image

input_folder = r'D:\Semester - 5\python internship\code files\task_7\images'
output_folder = 'resized_images'
output_size = (256, 256)
output_format = 'PNG'

for root, dirs, files in os.walk(input_folder):
    rel_path = os.path.relpath(root, input_folder)
    save_dir = os.path.join(output_folder, rel_path)
    os.makedirs(save_dir, exist_ok=True)

    for filename in files:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            img_path = os.path.join(root, filename)
            try:
                with Image.open(img_path) as img:
                    img_resized = img.resize(output_size)
                    base_name, _ = os.path.splitext(filename)
                    new_filename = f"{base_name}_resized.{output_format.lower()}"
                    output_path = os.path.join(save_dir, new_filename)
                    img_resized.save(output_path, output_format)
                    print(f"Resized and saved: {output_path}")
            except Exception as e:
                print(f"Error processing {img_path}: {e}")
