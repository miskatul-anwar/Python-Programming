import subprocess

import matplotlib.pyplot as plt
import pandas as pd


class Plotting:
    def __init__(self) -> None:
        try:
            self.df = pd.read_csv("data.csv")
        except FileNotFoundError as e:
            print(e, "not found")
            self.df = None

    def gen_latex(self) -> None:
        try:
            result = subprocess.run(
                ["xelatex", "document.tex"], capture_output=True, text=True
            )
            if result.returncode != 0:
                print("LaTeX compilation failed. Here's the output:")
                print(result.stderr)
            else:
                print("LaTeX compilation succeeded.")
        except FileNotFoundError:
            print("pdflatex not found. Make sure it's installed and in your PATH.")

    def pie_chart(self) -> None:
        if self.df is None:
            print("No data to plot")
            return
        amount = self.df["pie"].to_list()
        labels = self.df["labels"].to_list()
        plt.pie(amount, labels=labels, autopct="%1.1f%%", shadow=True, startangle=90)
        plt.savefig("pie.pdf", format="pdf")
        print("Pie chart created!")
        self.gen_latex()

    def bar_chart(self) -> None:
        if self.df is None:
            print("No data to plot")
            return
        amount = self.df["bar"].to_list()
        labels = self.df["labels"].to_list()
        plt.bar(labels, amount)
        plt.savefig("bar.pdf", format="pdf")
        print("Bar chart created!")
        self.gen_latex()

    def line_chart(self) -> None:
        if self.df is None:
            print("No data to plot")
            return
        amount = self.df["line"].to_list()
        labels = self.df["labels"].to_list()
        plt.plot(labels, amount)
        plt.savefig("line.pdf", format="pdf")
        print("Line chart created!")
        self.gen_latex()

    def choice(self) -> None:
        print("What would you like to plot?")
        print("1. Pie chart", end=" ")
        print("2. Bar chart", end=" ")
        print("3. Line chart")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                self.pie_chart()
            case 2:
                self.bar_chart()
            case 3:
                self.line_chart()
            case _:
                print("Invalid choice")
                self.choice()


def main() -> None:
    plotting = Plotting()
    plotting.choice()


if __name__ == "__main__":
    main()
