from collections import OrderedDict

MAX_SLOTS_INGREDIENT = 25
MAX_STACK_INGREDIENT = 25
MAX_SLOTS_POTION = 10
MAX_STACK_POTION = 10


class Inventory:
    def __init__(self, max_slots, max_stack):
        self.max_slots = max_slots
        self.max_stack = max_stack
        self.items = OrderedDict()

    def count(self, name):
        return self.items.get(name, 0)

    def add(self, name, quantity=1):
        if quantity <= 0:
            raise ValueError("Кількість має бути більшою за нуль.")
        current = self.count(name)
        room_in_stack = max(0, self.max_stack - current)
        to_existing = min(room_in_stack, quantity)
        new_quantity = quantity - to_existing
        if new_quantity and name not in self.items and len(self.items) >= self.max_slots:
            raise ValueError("Немає вільного слота в інвентарі.")
        if current + quantity > self.max_stack:
            raise ValueError(f"У слоті максимум {self.max_stack} предметів.")
        self.items[name] = current + quantity
        return quantity

    def remove(self, name, quantity=1):
        if quantity <= 0:
            raise ValueError("Кількість має бути більшою за нуль.")
        if self.count(name) < quantity:
            raise ValueError(f"Недостатньо предмета «{name}».")
        left = self.count(name) - quantity
        if left:
            self.items[name] = left
        else:
            del self.items[name]

    def has(self, name, quantity=1):
        return self.count(name) >= quantity

    def show(self):
        if not self.items:
            print("  (порожньо)")
            return
        for i, (name, quantity) in enumerate(self.items.items(), 1):
            print(f"  {i}. {name} — {quantity}/{self.max_stack}")

    def free_slots(self):
        return self.max_slots - len(self.items)


ingredients_inventory = Inventory(MAX_SLOTS_INGREDIENT, MAX_STACK_INGREDIENT)
potion_inventory = Inventory(MAX_SLOTS_POTION, MAX_STACK_POTION)
