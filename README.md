# Image Compressor

## Purpose

**Image Compressor** is a batch image processing tool that automatically compresses JPEG and PNG images while maintaining acceptable quality. It's designed to reduce image file sizes efficiently, making it ideal for optimizing photos for web deployment, reducing storage requirements, or preparing large image collections for cloud storage.

### Key Features
- **Batch Compression**: Process multiple images at once
- **Format Support**: JPEG, JPG, PNG, and WebP formats
- **Configurable Quality**: Fine-tune compression levels per format
- **Optimized JPEG**: Progressive encoding for better web performance
- **WebP Conversion**: Modern format with superior compression
- **Smart Resizing**: Automatic image scaling for web optimization
- **Format Detection**: Intelligent compression based on image type
- **Automatic Output**: Directory creation and error handling

## Requirements

- Python 3.11 or higher
- Pillow 12.1.0 or higher

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd img-compressor
```

2. Create a virtual environment (recommended):
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -e .
```

## Usage

### Basic Usage

Create directories for your images and run the script:

```bash
python main.py
```

The default configuration compresses images from:
- `images/Photos-1-001-1/` → `images/Photos-1-001-1/compressed_images/`
- `images/Photos-1-001/` → `images/Photos-1-001/compressed_images/`

### Customizing Compression

Edit `main.py` to specify custom input/output directories and quality settings:

```python
from compress_image import batch_compress

batch_compress(
    input_folder="path/to/input",
    output_folder="path/to/output",
    quality=88  # 0-100, higher = better quality but larger file size
)
```

### WebP Conversion (Advanced)

Convert images to WebP format with automatic resizing and intelligent compression:

```python
from compress_image import batch_compress_to_webp

batch_compress_to_webp(
    input_folder="path/to/input",
    output_folder="path/to/output",
    quality=90,           # 75-85 recommended for photos
    max_width=1920,       # Max width for web images
    max_height=1080,      # Max height for web images
    lossless_for_png=True # Use lossless for PNGs (logos, UI)
)
```

### Function Parameters

**batch_compress():**
- `input_folder` (str): Path to folder containing images to compress
- `output_folder` (str): Path where compressed images will be saved
- `quality` (int, default=88): Quality level for JPEG compression (1-100)

**batch_compress_to_webp():**
- `input_folder` (str): Path to folder containing images to convert
- `output_folder` (str): Path where WebP images will be saved
- `quality` (int, default=80): WebP quality level (75-85 ideal for web)
- `max_width` (int, default=1920): Maximum image width for web
- `max_height` (int, default=1080): Maximum image height for web
- `lossless_for_png` (bool, default=True): Use lossless compression for PNG files

## How It Works

### Standard Compression

1. Scans the input folder for supported image formats (.jpg, .jpeg, .png)
2. Opens each image using Pillow
3. Applies format-specific compression:
   - **JPEG/JPG**: Quality reduction with optimization and progressive encoding
   - **PNG**: Maximum compression level with optimization
4. Saves compressed images to the output folder
5. Prints confirmation message for each processed image

### WebP Conversion

1. Scans the input folder for image files (.jpg, .jpeg, .png, .webp)
2. Converts image color modes for WebP compatibility (RGBA, Palette → RGBA/RGB)
3. Resizes images for web using LANCZOS high-quality resampling
4. Applies intelligent compression:
   - **Photos (JPEG)**: Lossy WebP compression (quality 75-85 recommended)
   - **Graphics (PNG)**: Lossless WebP compression (preserves transparency)
5. Saves optimized WebP images to output folder
6. Reports results with error handling for unsupported files

## WebP Format Advantages

WebP is a modern image format that provides superior compression while maintaining quality:

### File Size Reduction
- **25-35% smaller** than JPEG at equivalent quality
- **15-20% smaller** than PNG for most images
- Significant bandwidth savings for web delivery

### Quality Benefits
- Supports both lossy and lossless compression
- Better quality preservation at lower file sizes
- Maintains color accuracy and detail

### Web Performance
- Faster page load times due to smaller files
- Reduced server bandwidth costs
- Improved Core Web Vitals (LCP, FID, CLS)
- Better mobile experience

### Modern Browser Support
- **95%+ browser coverage** across modern browsers
- Supported in Chrome, Firefox, Edge, Safari 16+
- Fallback support available for older browsers

### Use Cases
- **E-commerce**: Faster product image loading
- **Photography**: High-quality albums with smaller files
- **Web apps**: Reduced data usage on mobile networks
- **Cloud storage**: Efficient backup of photo libraries
- **Content sites**: Faster page rendering

## Project Structure

```
img-compressor/
├── main.py                 # Entry point and configuration
├── compress_image.py       # Core compression logic
├── pyproject.toml          # Project metadata and dependencies
└── README.md              # This file
```

## License

Add your license information here.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
