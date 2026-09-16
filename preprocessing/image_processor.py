import cv2


class ImageProcessor:
    """Handles basic image preprocessing operations."""

    def resize(self, image, width=640):
        height, original_width = image.shape[:2]

        ratio = width / original_width
        new_height = int(height * ratio)

        return cv2.resize(image, (width, new_height))

    def grayscale(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def denoise(self, image):
        return cv2.GaussianBlur(image, (5, 5), 0)

    def enhance_contrast(self, image):
        gray = self.grayscale(image)
        return cv2.equalizeHist(gray)

    def process(self, image):
        resized = self.resize(image)
        denoised = self.denoise(resized)
        enhanced = self.enhance_contrast(denoised)

        return {
            "resized": resized,
            "denoised": denoised,
            "enhanced": enhanced
        }