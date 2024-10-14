from random import choice as rc
from tqdm import tqdm as tq
from pyfiglet import figlet_format as ft
import plotly.express as px
import pandas as pd

MAX_LIM: int = 10000000
cnt1: int = 0
cnt2: int = 0
draw: int = 0


def printf(text: str):
    ascii_art = ft(text, font="block", width=100, justify="center")
    print(ascii_art)


def drawBar(cnt1: int, cnt2: int, draw: int) -> None:
    # Prepare data for the bar chart
    data = {"Results": ["Player 01", "Player 02", "Draw"], "Counts": [cnt1, cnt2, draw]}

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Create a bar chart
    fig = px.bar(
        df,
        x="Results",
        y="Counts",
        title="Results of Head and Tail Simulation",
        labels={"Counts": "Number of Wins/Draws"},
        color="Results",
        color_discrete_sequence=px.colors.qualitative.Plotly,
    )

    # Show the figure
    fig.show()


def main():
    printf("Head And Tail")
    global cnt1, cnt2, draw
    for _ in tq(range(MAX_LIM)):
        player1 = rc(["H", "T"])
        player2 = rc(["H", "T"])
        if player1 != player2:
            if player1 == "H":
                cnt1 += 1
            else:
                cnt2 += 1
        else:
            draw += 1

    win1: float = 100 * cnt1 / MAX_LIM
    win2: float = 100 * cnt2 / MAX_LIM
    nowin: float = 100 * draw / MAX_LIM
    print(
        f"Results are: \nPlayer 01: {win1:.2f}%\nPlayer 02: {win2:.2f}%\nDraw: {nowin:.2f}%"
    )

    # Call the drawBar function to display the bar chart
    drawBar(cnt1, cnt2, draw)


if __name__ == "__main__":
    main()
