import tqdm
import random

n_lim = 10000000
total_sum = 0  # Renamed to avoid shadowing the built-in `sum` function


def main():
    global total_sum  # Declare `total_sum` as global to modify it
    for _ in tqdm.tqdm(range(n_lim)):
        total_sum += random.randint(0, 100)
    print(total_sum)


if __name__ == "__main__":
    main()
