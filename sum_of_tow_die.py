import random
from tqdm import tqdm

N_TRIALS = 10000000
TARGET_SUM = 7


def main():
    n_events = 0
    for _ in tqdm(range(N_TRIALS)):
        dice_total = run_experiment()
        if dice_total == TARGET_SUM:
            n_events += 1
    pre_e = n_events / N_TRIALS
    print(f"After {N_TRIALS} trials")
    print("P(E) =", pre_e)


def run_experiment():
    d_1 = roll_dice()
    d_2 = roll_dice()
    return d_1 + d_2


def roll_dice():
    return random.choice([1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    main()
