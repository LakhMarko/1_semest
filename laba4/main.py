"""Точка входу: запускає демонстрації 10 сторонніх і 5 вбудованих модулів."""
from func01_requests import demo_requests
from func02_numpy import demo_numpy
from func03_pandas import demo_pandas
from func04_matplotlib import demo_matplotlib
from func05_pillow import demo_pillow
from func06_qrcode import demo_qrcode
from func07_colorama import demo_colorama
from func08_rich import demo_rich
from func09_tqdm import demo_tqdm
from func10_dotenv import demo_dotenv
from func11_math import demo_math
from func12_random import demo_random
from func13_datetime import demo_datetime
from func14_json import demo_json
from func15_os import demo_os

def main():
    demos = [
        ("requests", demo_requests), ("numpy", demo_numpy),
        ("pandas", demo_pandas), ("matplotlib", demo_matplotlib),
        ("Pillow", demo_pillow), ("qrcode", demo_qrcode),
        ("colorama", demo_colorama), ("rich", demo_rich),
        ("tqdm", demo_tqdm), ("python-dotenv", demo_dotenv),
        ("math", demo_math), ("random", demo_random),
        ("datetime", demo_datetime), ("json", demo_json),
        ("os", demo_os),
    ]
    for name, function in demos:
        print(f"\\n--- {name} ---")
        try:
            function()
        except Exception as error:
            print(f"Помилка в модулі {name}: {error}")

if __name__ == "__main__":
    main()
