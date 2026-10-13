"""Вбудований модуль datetime."""
from datetime import datetime

def demo_datetime():
    print("Поточні дата й час:", datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
