import base64
from PIL import Image
import io

class VisionProcessor:
    @staticmethod
    def encode_image_to_base64(image_path: str):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    @staticmethod
    def optimize_for_llm(image_path: str, output_path: str):
        # Resizing and compressing to save tokens while maintaining high-fidelity details
        with Image.open(image_path) as img:
            img.thumbnail((1024, 1024))
            img.save(output_path, "PNG", quality=85)
