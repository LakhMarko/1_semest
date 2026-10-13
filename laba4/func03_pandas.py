"""Стороння бібліотека pandas."""
import pandas as pd

def demo_pandas():
    table = pd.DataFrame({"Предмет": ["Математика", "Фізика"], "Оцінка": [10, 11]})
    print(table.to_string(index=False))
