def Jaccard(str1, str2):
    s1 = set(str1.split(" "))
    s2 = set(str2.split(" "))
    union = len(s1 | s2)
    intersect = len(s1 & s2)
    if union == 0:
        return 0.0
    return intersect / union


def main():
    s1 = "Data is the new oil of digital economy"
    s2 = "Data is a new oil"
    print(
        "The Jaccard similarity: \n"
        + "-" * 22
        + "\n" * 2
        + s1
        + "\n"
        + s2
        + "\n"
        + "= ",
        end=" ",
    )
    print(Jaccard(s1, s2))


if __name__ == "__main__":
    main()
