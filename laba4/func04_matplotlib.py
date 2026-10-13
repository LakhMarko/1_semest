"""Стороння бібліотека matplotlib."""
import matplotlib
matplotlib.use("Agg")  # Побудова графіка без окремого вікна.
import matplotlib.pyplot as plt

def demo_matplotlib():
    plt.plot([1, 2, 3], [2, 4, 3], marker="o")
    plt.title("Приклад графіка")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.savefig("demo_chart.png")
    plt.close()
    print("Графік збережено у файл demo_chart.png")
