from PIL import Image
import os

def batch_compress(input_folder, output_folder, quality=88):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            img = Image.open(input_path)

            if img.format in ["JPEG", "JPG"]:
                img.save(output_path, "JPEG", quality=quality, optimize=True, progressive=True)
            elif img.format == "PNG":
                img.save(output_path, "PNG", optimize=True, compress_level=9)

            print(f"Compressed: {filename}")
