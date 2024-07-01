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
        return f"Item('{self.name}',{self.quantity})"


def main():
    item1 = Item("Phone", 100, 5)
    print(item1.price)
    print(item1.quantity)
    print(item1.calculate_price())
    item2 = Item("Calculator", 100, 5)
    item1.pay_rate = 0.7
    print(item1.calculate_price())
    print(item2.calculate_price())
    print(Item.all)


if __name__ == "__main__":
    main()
