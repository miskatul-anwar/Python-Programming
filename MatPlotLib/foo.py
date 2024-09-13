from matplotlib import pyplot as plt
import numpy as np


class i2dplot:
    def __init__(self) -> None:
        self.x = []
        self.y = []
        self.z = []

    def start_plot(self) -> None:
        self.x = np.linspace(0, 10 * np.pi, 1000)
        self.y = np.sin(self.x)
        fig, ax = plt.subplots()
        ax.plot(self.x, self.y)
        ax.set_title("Sine Wave")
        plt.show()
        plt.close(fig)

    def bar_plot(self) -> None:
        self.x = np.linspace(1, 10, 10)
        self.y = np.random.uniform(1, 10, 10)
        fig, ax = plt.subplots()
        ax.bar(self.x, self.y)
        ax.set_title("Bar Plot")
        plt.show()
        plt.close(fig)

    def image(self) -> None:
        self.z = np.random.uniform(0, 1, (8, 8))
        fig, ax = plt.subplots()
        ax.imshow(self.z, cmap="viridis")
        ax.set_title("Image")
        plt.show()
        plt.close(fig)

    def piechart(self) -> None:
        self.z = np.random.uniform(0, 1, 4)
        fig, ax = plt.subplots()
        ax.pie(self.z, labels=["A", "B", "C", "D"], autopct="%1.1f%%")
        ax.set_title("Pie Chart")
        plt.show()
        plt.close(fig)

    def histogram(self) -> None:
        self.z = np.random.normal(0, 1, 100)
        fig, ax = plt.subplots()
        ax.hist(self.z, bins=10)
        ax.set_title("Histogram")
        plt.show()
        plt.close(fig)

    def errorbar(self) -> None:
        self.x = np.arange(5)
        self.y = np.random.uniform(0, 1, 5)
        fig, ax = plt.subplots()
        ax.errorbar(self.x, self.y, self.y / 4)
        plt.show()
        plt.close()

    def contourf(self) -> None:
        self.z = np.random.uniform(0, 1, (8, 8))
        fig, ax = plt.subplots()
        ax.contourf(self.z)
        plt.show()
        plt.close()

    def boxplot(self) -> None:
        self.z = np.random.normal(0, 1, (100, 3))
        fig, ax = plt.subplots()
        ax.boxplot(self.z)
        plt.show()
        fig.savefig("mypic.png", dpi=300)
        plt.close()

    def bar_plot_colored(self) -> None:
        categories = ["A", "B", "C"]
        colors = ["red", "blue", "orange"]
        values = [12, 13, 14]
        plt.bar(categories, values, color=colors)
        plt.show()
        plt.close()


def main():
    plot = i2dplot()
    plot.bar_plot_colored()


if __name__ == "__main__":
    main()
