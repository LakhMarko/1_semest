from all_potions import potions


def normalize_combo(names):
    return tuple(sorted(names))


def find_potion(selected_ingredients):
    selected = normalize_combo(selected_ingredients)
    for potion in potions:
        for recipe in potion["recipes"]:
            if normalize_combo(recipe) == selected:
                return potion
    return None


def brew(selected_ingredients, ingredient_inventory, potion_inventory):
    """Повертає повідомлення; не повертає і не друкує склад рецепта."""
    if len(selected_ingredients) < 1:
        raise ValueError("Спочатку вибери хоча б один інгредієнт.")
    if len(selected_ingredients) != len(set(selected_ingredients)):
        raise ValueError("Один і той самий інгредієнт не можна вибирати двічі в одному експерименті.")
    for name in selected_ingredients:
        if not ingredient_inventory.has(name):
            raise ValueError(f"У тебе немає інгредієнта «{name}».")

    potion = find_potion(selected_ingredients)
    if potion is None:
        # Невдалий експеримент також витрачає вибрані інгредієнти.
        for name in selected_ingredients:
            ingredient_inventory.remove(name)
        return None

    # Перевіряємо місце перед тим, як витрачати інгредієнти.
    current = potion_inventory.count(potion["name"])
    if current >= potion_inventory.max_stack:
        raise ValueError("Стак цього зілля вже повний.")
    if current == 0 and potion_inventory.free_slots() <= 0:
        raise ValueError("Немає вільного слота для нового виду зілля.")

    for name in selected_ingredients:
        ingredient_inventory.remove(name)
    potion_inventory.add(potion["name"])
    return {"name": potion["name"], "price": potion["price"]}