class Item:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_price(self) -> float:
        print(f"The Product Name: {self.name}")
        return self.price * self.quantity


def main():
    item1 = Item("Phone", 100, 5)
    print(item1.price)
    print(item1.quantity)
    print(item1.calculate_price())


if __name__ == "__main__":
    main()
