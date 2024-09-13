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

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"


class Phone(Item):
    pass


def main():
    phone1 = Phone("miskat", 500, 5)
    print(phone1.calculate_price())


if __name__ == "__main__":
    main()
