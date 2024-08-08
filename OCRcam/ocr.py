import pytesseract

class OCRProcessor:
    def extract_text(self, image):
        return pytesseract.image_to_string(image)