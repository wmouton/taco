import os
from PIL import Image
import argparse
from pathlib import Path

# Constants
OUTPUT_DIR = "webp_output"  # Directory to save WebP images
WEBP_QUALITY = 90  # WebP quality (0-100)


def convert_to_webp(input_path, output_dir, quality):
    """
    Convert an image to WebP format and save it to the output directory.
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Create the output file path
            output_path = Path(output_dir) / (Path(input_path).stem + ".webp")

            # Save the image in WebP format with the specified quality
            img.save(output_path, "WEBP", quality=quality)

            print(f"Converted {input_path} to {output_path}")
    except Exception as e:
        print(f"Error converting {input_path}: {e}")


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Mass convert images to WebP format.")
    parser.add_argument("patterns", nargs="+",
                        help="Image file patterns (e.g., *.png, *.jpg)")
    args = parser.parse_args()

    # Create the output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Process each file pattern
    for pattern in args.patterns:
        for input_path in Path(".").glob(pattern):
            if input_path.is_file():
                convert_to_webp(input_path, OUTPUT_DIR, WEBP_QUALITY)


if __name__ == "__main__":
    main()
