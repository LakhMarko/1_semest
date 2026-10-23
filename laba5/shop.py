"""Продаж зіль наприкінці дня."""
from all_potions import potions


def sell_potions(inventory, gold):
    prices = {p["name"]: p["price"] for p in potions}
    while True:
        print("\n--- Продаж зіль ---")
        if not inventory.items:
            print("У тебе немає зіль для продажу.")
            return gold
        for i, (name, quantity) in enumerate(inventory.items.items(), 1):
            print(f"{i}. {name} — {quantity} шт. | {prices.get(name, 0)} золота за штуку")
        print("0. Завершити продаж")
        try:
            choice = input("Номер зілля для продажу: ").strip()
            if choice == "0":
                return gold
            index = int(choice)
            names = list(inventory.items.keys())
            if not 1 <= index <= len(names):
                print("Немає такого пункту.")
                continue
            name = names[index - 1]
            quantity = int(input(f"Скільки продати (1–{inventory.count(name)}): "))
            if quantity < 1 or quantity > inventory.count(name):
                print("Некоректна кількість.")
                continue
            price = prices.get(name, 0)
            inventory.remove(name, quantity)
            earned = price * quantity
            gold += earned
            print(f"Продано: {quantity} шт. Отримано {earned} золота. Баланс: {gold}.")
        except ValueError as error:
            print(f"Помилка введення: {error}")
        except (EOFError, KeyboardInterrupt):
            print("\nПродаж завершено.")
            return gold