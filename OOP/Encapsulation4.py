class Item:
    pay_rate = 0.8

    def __init__(self, name: str, price: float, quantity: int) -> None:
        assert price >= 0, f"Price {price} is not valid"
        assert quantity >= 0, f"Quantity {quantity} is not valid"
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_price(self) -> float:
        print(f"The Product Name: {self.name}")
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate


def main():
    item1 = Item("Phone", 100, 5)
    # print(Item.__dict__)
    print(item1.price)
    print(item1.quantity)
    print(item1.calculate_price())
    print(item1.apply_discount())
    print(item1.calculate_price())


if __name__ == "__main__":
    main()
