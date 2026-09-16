import numpy as np
from preprocessing.image_processor import ImageProcessor


def main():
    processor = ImageProcessor()

    # Create a sample image
    image = np.zeros((480, 640, 3), dtype=np.uint8)

    results = processor.process(image)

    print("Preprocessing test successful")
    print("Original:", image.shape)
    print("Resized:", results["resized"].shape)
    print("Enhanced:", results["enhanced"].shape)


if __name__ == "__main__":
    main()