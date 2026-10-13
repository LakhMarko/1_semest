"""Стороння бібліотека Pillow (імпорт PIL)."""
from PIL import Image

def demo_pillow():
    image = Image.new("RGB", (200, 100), color="skyblue")
    image.save("demo_image.png")
    print("Зображення створено: demo_image.png")
