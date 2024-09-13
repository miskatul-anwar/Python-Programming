import re


def valid_five_digit_code(number: str) -> bool:
    check = re.compile(r"^\d{5}$")
    return bool(check.match(number))


def main() -> int:
    take_input = input("Enter a 5-digit code: ")
    if valid_five_digit_code(take_input):
        print("You're right")
    else:
        print("You're mad")
    return 0


if __name__ == "__main__":
    main()
