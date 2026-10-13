"""Стороння бібліотека qrcode."""
import qrcode

def demo_qrcode():
    image = qrcode.make("Python Library Demo")
    image.save("demo_qr.png")
    print("QR-код збережено: demo_qr.png")
