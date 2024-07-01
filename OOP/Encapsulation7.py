import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        assert price >= 0, f"Price {price} is not valid"
        assert quantity >= 0, f"Quantity {quantity} is not valid"
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_price(self) -> float:
        print(f"The Product Name: {self.name}")
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=str(item.get("name")),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"


def main():
    Item.instantiate_from_csv()
    for item in Item.all:
        print(item)


if __name__ == "__main__":
    main()
