import pandas as pd


def sol(s: str) -> dict:
    count = dict()
    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    return count


def main() -> None:
    s = str(input("Enter the string: "))
    count_dict = dict(sol(s))
    dataFrame = pd.DataFrame(list(count_dict.items()), columns=["Character", "Count"])
    print(dataFrame)


if __name__ == "__main__":
    main()
