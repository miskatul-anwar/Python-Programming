from math import sqrt


class func:
    def __init__(self, str1: str, str2: str) -> None:
        self.str1 = str1
        self.str2 = str2

    def word_count(self, tar: str) -> dict:
        freq = {}
        for it in tar.split():
            if it in freq:
                freq[it] += 1
            else:
                freq[it] = 1
        return freq

    def cosine_similarity(self) -> float:
        map1 = self.word_count(self.str1)
        map2 = self.word_count(self.str2)
        dot_product = sum(map1[word] * map2.get(word, 0) for word in map1)
        magnitude1 = sqrt(sum(freq**2 for freq in map1.values()))
        magnitude2 = sqrt(sum(freq**2 for freq in map2.values()))
        if magnitude1 * magnitude2 == 0:
            return 0.0
        return dot_product / (magnitude1 * magnitude2)

    def __repr__(self) -> str:
        return f"the given strings are:\n 1. {self.str1}\n 2. {self.str2}\n"

    @property  # works like getters
    def values(self) -> list:
        return [self.str1, self.str2]

    def setvalues(self, str1: str, str2: str) -> None:
        self.str1 = str1
        self.str2 = str2


def main():
    doc1 = str("the best data science course")
    doc2 = str("data science is popular")
    f = func(doc1, doc2)
    print(f"{f}{f.cosine_similarity()}")
    f.setvalues("aaa", "aaa")
    print(f"{f}{f.cosine_similarity()}")


if __name__ == "__main__":
    main()
