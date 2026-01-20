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
            
            
def batch_compress_to_webp(
    input_folder,
    output_folder,
    quality=80,
    max_width=1920,
    max_height=1080,
    lossless_for_png=True
):
    """
    Batch compress images and convert to WebP.

    :param input_folder: Folder with original images
    :param output_folder: Folder to save WebP images
    :param quality: WebP quality (75–85 ideal for web)
    :param max_width: Max width for web images
    :param max_height: Max height for web images
    :param lossless_for_png: Use lossless WebP for PNGs (logos, UI)
    """

    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if not filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            continue

        input_path = os.path.join(input_folder, filename)

        try:
            img = Image.open(input_path)

            # Convert modes for WebP compatibility
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGBA")
            else:
                img = img.convert("RGB")

            # Resize for web
            img.thumbnail(
                (max_width, max_height),
                Image.LANCZOS
            )

            name, _ = os.path.splitext(filename)
            output_path = os.path.join(output_folder, f"{name}.webp")

            # Decide lossless vs lossy
            if input_path.lower().endswith(".png") and lossless_for_png:
                img.save(
                    output_path,
                    "WEBP",
                    lossless=True,
                    method=6
                )
            else:
                img.save(
                    output_path,
                    "WEBP",
                    quality=quality,
                    method=6
                )

            print(f"Converted → WebP: {filename}")

        except Exception as e:
            print(f"Failed to process {filename}: {e}")

    print("WebP conversion complete.")
