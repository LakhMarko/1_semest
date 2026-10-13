"""Стороння бібліотека tqdm."""
from tqdm import tqdm

def demo_tqdm():
    for _ in tqdm(range(5), desc="Демонстрація"):
        pass
    print("Цикл завершено.")
