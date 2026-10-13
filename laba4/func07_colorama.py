"""Стороння бібліотека colorama."""
from colorama import init, Fore, Style

def demo_colorama():
    init(autoreset=True)
    print(Fore.GREEN + "Цей текст виведено зеленим кольором." + Style.RESET_ALL)
