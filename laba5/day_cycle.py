"""Ігрові дні та щоденна видача п'яти інгредієнтів."""
import random
from list_of_ingredients import all_ingredients


def start_new_day(day_number, inventory):
    print(f"\n========== ДЕНЬ {day_number} ==========")
    received = []
    for _ in range(5):
        # Повторна спроба, якщо предмет не вміщується або його стак повний.
        candidates = list(all_ingredients)
        random.shuffle(candidates)
        added = False
        for ingredient in candidates:
            count = inventory.count(ingredient)
            if count < inventory.max_stack and (
                count > 0 or inventory.free_slots() > 0
            ):
                try:
                    inventory.add(ingredient, 1)
                    received.append(ingredient)
                    added = True
                    break
                except (ValueError, TypeError) as error:
                    print(f"Не вдалося отримати інгредієнт: {error}")
        if not added:
            print("Інвентар переповнений: не всі щоденні інгредієнти вдалося отримати.")
            break
    if received:
        print("Сьогодні отримано:")
        for item in received:
            print(f"  - {item}")
