# Початкові дані товарів
vegetable = {'name': 'Овоч', 'value': 15.00, 'quantity': 43}
milky = {'name': 'Молоко', 'value': 55.00, 'quantity': 27}
meat = {'name': 'М\'ясо', 'value': 105.00, 'quantity': 36}

products = {'1': vegetable, '2': milky, '3': meat}
cart = {'1': 0, '2': 0, '3': 0}  # Кошик збереже кількість вибраного товару

password = '123'

# Лямбда-функції
format_price = lambda price: f"{price:.2f}грн"
not_true = lambda: print("\n[!] Невірний вибір. Спробуйте ще раз.\n")


def first_scrine():
    """Екран 0: Головне меню"""
    while True:
        print("\n--- ГОЛОВНЕ МЕНЮ ---")
        print("1) Список товарів\n2) Кошик\n3) Режим адміністратора\n4) Вийти з програми")
        action = input("Оберіть дію: ")

        if action == '1':
            cataloge()
        elif action == '2':
            pocket()
        elif action == '3':
            admin_mode()
        elif action == '4':
            print("Дякуємо за відвідування магазину!")
            break
        else:
            not_true()


def cataloge():
    """Екран 1: Каталог товарів (Додавання в кошик)"""
    while True:
        print("\n--- КАТАЛОГ ТОВАРІВ ---")
        print(f"1) Овоч - {format_price(vegetable['value'])}")
        print(f"2) Молоко - {format_price(milky['value'])}")
        print(f"3) М'ясо - {format_price(meat['value'])}")
        print("4) На головну")

        choice = input("Оберіть товар для додавання в кошик: ")

        if choice in ['1', '2', '3']:
            prod = products[choice]
            if prod['quantity'] > cart[choice]:
                cart[choice] += 1
                print(f"-> {prod['name']} додано до кошика! (У кошику: {cart[choice]})")
            else:
                print(f"[!] Немає більше товару '{prod['name']}' на складі!")
        elif choice == '4':
            break
        else:
            not_true()


def pocket():
    """Екран 2: Кошик (Видалення, купівля)"""
    while True:
        print("\n--- КОШИК ---")
        total_sum = 0

        # Відображення товарів у кошику
        for key, count in cart.items():
            prod_name = products[key]['name']
            print(f"{key}) {prod_name} — кількість: {count}")
            total_sum += count * products[key]['value']

        print(f"\nСУМА: {format_price(total_sum)}")
        print("4) Купити")
        print("5) На головну")

        choice = input("Оберіть номер товару для зменшення/видалення або дію (4-5): ")

        if choice in ['1', '2', '3']:
            if cart[choice] > 0:
                cart[choice] -= 1
                print(f"-> 1 шт. {products[choice]['name']} видалено з кошика.")
            else:
                print("[!] Цього товару немає в кошику.")
        elif choice == '4':
            if total_sum == 0:
                print("[!] ваш кошик порожній!")
            else:
                # Оформлення покупки та списання товарів зі складу
                for key, count in cart.items():
                    products[key]['quantity'] -= count
                    cart[key] = 0
                print(f"\n Покупка успішна! Дякуємо! Сплачено: {format_price(total_sum)}")
                break
        elif choice == '5':
            break
        else:
            not_true()


def admin_mode():
    """Екран 3: Режим адміністратора (Залишки товарів)"""
    entered_password = input("Введіть пароль адміністратора: ")
    if entered_password != password:
        print("[!] Невірний пароль!")
        return

    while True:
        print("\n--- АДМІН-ПАНЕЛЬ (ЗАЛИШКИ) ---")
        print(f"1) Овоч — залишок: {vegetable['quantity']} шт.")
        print(f"2) Молоко — залишок: {milky['quantity']} шт.")
        print(f"3) М'ясо — залишок: {meat['quantity']} шт.")
        print("4) На головну")

        choice = input("Оберіть дію: ")
        if choice == '4':
            break
        else:
            not_true()


# Запуск програми
first_scrine()