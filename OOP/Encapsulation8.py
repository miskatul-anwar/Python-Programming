import csv
from typing import List, Dict, Any


class Item:
    pay_rate = 0.8
    all: List["Item"] = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        assert price >= 0, f"Price {price} is not valid"
        assert quantity >= 0, f"Quantity {quantity} is not valid"
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_price(self) -> float:
        """Calculate total price of the item based on quantity."""
        print(f"The Product Name: {self.name}")
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """Apply a discount to the item price."""
        self.price = self.price * Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_path: str = "items.csv") -> None:
        """Instantiate Item objects from a CSV file."""
        try:
            with open(file_path, "r") as f:
                reader = csv.DictReader(f)
                items = list(reader)
            for item in items:
                Item(
                    name=str(item.get("name")),
                    price=float(item.get("price")),
                    quantity=int(item.get("quantity")),
                )
        except FileNotFoundError:
            print(f"The file {file_path} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def is_integer(num: Any) -> bool:
        """Check if the number is an integer."""
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self) -> str:
        """Return a string representation of the Item object."""
        return f"Item('{self.name}', {self.price}, {self.quantity})"


def main():
    Item.instantiate_from_csv()
    for item in Item.all:
        print(item)
    print(Item.is_integer(6))
    print(Item.is_integer(6.0))
    print(Item.is_integer(6.5))


if __name__ == "__main__":
    main()
