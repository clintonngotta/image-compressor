from compress_image import batch_compress
def main():
    print("Hello from img-compressor!")
    batch_compress("images/Photos-1-001-1", "images/Photos-1-001-1/compressed_images")
    batch_compress("images/Photos-1-001", "images/Photos-1-001/compressed_images")

if __name__ == "__main__":
    main()
