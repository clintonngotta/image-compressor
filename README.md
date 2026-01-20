# Image Compressor

## Purpose

**Image Compressor** is a batch image processing tool that automatically compresses JPEG and PNG images while maintaining acceptable quality. It's designed to reduce image file sizes efficiently, making it ideal for optimizing photos for web deployment, reducing storage requirements, or preparing large image collections for cloud storage.

### Key Features
- Batch compress multiple images at once
- Support for JPEG, JPG, and PNG formats
- Configurable quality settings
- Optimized compression with progressive JPEG support
- Automatic directory creation for output
- Simple and straightforward command-line interface

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

### Function Parameters

- `input_folder` (str): Path to folder containing images to compress
- `output_folder` (str): Path where compressed images will be saved
- `quality` (int, default=88): Quality level for JPEG compression (1-100)

## How It Works

1. Scans the input folder for supported image formats (.jpg, .jpeg, .png)
2. Opens each image using Pillow
3. Applies format-specific compression:
   - **JPEG/JPG**: Quality reduction with optimization and progressive encoding
   - **PNG**: Maximum compression level with optimization
4. Saves compressed images to the output folder
5. Prints confirmation message for each processed image

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
