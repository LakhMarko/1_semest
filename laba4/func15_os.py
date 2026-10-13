"""Вбудований модуль os."""
import os

def demo_os():
    print("Поточна папка:", os.getcwd())
    print("Кількість елементів у папці:", len(os.listdir(".")))
