
"""Текстова RPG: Алхімік."""
from inventory_list import ingredients_inventory, potion_inventory
from list_of_ingredients import all_ingredients
from all_potions import potions
from alchemy import brew
from day_cycle import start_new_day
from shop import sell_potions


def choose_ingredients():
    chosen = []
    while True:
        print("\nТвої інгредієнти:")
        ingredients_inventory.show()
        print("Введи номер інгредієнта, щоб додати його до експерименту.")
        print("Введи 0, щоб завершити вибір.")
        try:
            choice = input("Вибір: ").strip()
            if choice == "0":
                return chosen
            index = int(choice)
            names = list(ingredients_inventory.items.keys())
            if not 1 <= index <= len(names):
                print("Немає такого пункту.")
                continue
            name = names[index - 1]
            if name in chosen:
                print("Цей інгредієнт уже вибраний.")
                continue
            chosen.append(name)
            print(f"Додано до експерименту: {name}")
        except ValueError:
            print("Введи номер зі списку.")
        except (EOFError, KeyboardInterrupt):
            return chosen


def show_status(day, gold):
    print(f"\nДень: {day} | Золото: {gold}")
    print(f"Інгредієнти: {len(ingredients_inventory.items)}/{ingredients_inventory.max_slots} слотів")
    print(f"Зілля: {len(potion_inventory.items)}/{potion_inventory.max_slots} слотів")


def main():
    day = 0
    gold = 0
    print("=" * 42)
    print("       АЛХІМІК: ШЛЯХ ДО ВЕЛИКОГО ВІДКРИТТЯ")
    print("=" * 42)
    print("Твоя мета — створити Філософський камінь або Зілля життя.")
    print("Рецепти приховані: експериментуй і запам'ятовуй свої відкриття.")
    print("Гра не має обмеження на кількість днів.")

    while True:
        try:
            day += 1
            start_new_day(day, ingredients_inventory)
            while True:
                show_status(day, gold)
                print("\n1. Переглянути інвентар інгредієнтів")
                print("2. Переглянути інвентар зіль")
                print("3. Провести алхімічний експеримент")
                print("4. Завершити день і перейти до продажу")
                print("5. Вийти з гри")
                choice = input("Обери дію: ").strip()

                if choice == "1":
                    ingredients_inventory.show()
                elif choice == "2":
                    potion_inventory.show()
                elif choice == "3":
                    chosen = choose_ingredients()
                    if not chosen:
                        print("Експеримент скасовано.")
                        continue
                    try:
                        result = brew(chosen, ingredients_inventory, potion_inventory)
                        if result:
                            print(f"\nУСПІХ! Ти створив(ла): {result['name']}!")
                            print(f"Орієнтовна ціна продажу: {result['price']} золота.")
                            # Перемога перевіряється відразу, рецепт не розкривається.
                            if result["name"] in ("Філософський камінь", "Зілля життя"):
                                print("\n" + "=" * 42)
                                print(f"ПЕРЕМОГА! Ти створив(ла): {result['name']}!")
                                print(f"Твій шлях алхіміка завершився на {day}-й день.")
                                print(f"Зібране золото: {gold}.")
                                print("=" * 42)
                                return
                        else:
                            print("Суміш не дала бажаного результату. Інгредієнти витрачено.")
                    except (ValueError, TypeError) as error:
                        print(f"Не вдалося провести експеримент: {error}")
                elif choice == "4":
                    gold = sell_potions(potion_inventory, gold)
                    break
                elif choice == "5":
                    print("Ти залишив(ла) лабораторію. До нових відкриттів!")
                    return
                else:
                    print("Невідома команда. Спробуй ще раз.")
        except (EOFError, KeyboardInterrupt):
            print("\nГру завершено.")
            return
        except Exception as error:
            # Запобіжник, щоб несподівана помилка не закривала гру мовчки.
            print(f"Сталася непередбачена помилка: {error}")
            print("Спробуй продовжити гру або перезапустити програму.")


if __name__ == "__main__":
    main()