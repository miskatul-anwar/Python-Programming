import subprocess
import pandas as pd
import plotly.express as px
import os
import glob


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
            self.cleanup_files()  # Clean up after LaTeX processing
        except FileNotFoundError:
            print("xelatex not found. Make sure it's installed and in your PATH.")

    def cleanup_files(self) -> None:
        # List of allowed file extensions
        allowed_extensions = [".tex", ".csv", ".py", ".pdf", ".png"]

        # Get all files in the current directory
        all_files = glob.glob("*")

        for file in all_files:
            # Check if file is not one of the allowed extensions
            if not any(file.endswith(ext) for ext in allowed_extensions):
                os.remove(file)  # Delete the file
                print(f"Deleted {file}")

    def pie_chart(self) -> None:
        if self.df is None:
            print("No data to plot")
            return
        fig = px.pie(self.df, names="labels", values="pie", title="Pie Chart")
        fig.write_image("pie.pdf")
        print("Pie chart created!")
        self.gen_latex()

    def bar_chart(self) -> None:
        if self.df is None:
            print("No data to plot")
            return
        fig = px.bar(self.df, x="labels", y="bar", title="Bar Chart")
        fig.write_image("bar.pdf")
        print("Bar chart created!")
        self.gen_latex()

    def line_chart(self) -> None:
        if self.df is None:
            print("No data to plot")
            return
        fig = px.line(self.df, x="labels", y="line", title="Line Chart")
        fig.write_image("line.pdf")
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
