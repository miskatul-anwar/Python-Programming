import threading
import time


def walk_dog(name: str) -> None:
    time.sleep(1)
    print("walking with " + name)


def take_out_trash(name: str) -> None:
    time.sleep(2)
    print("Taking the trash to " + name)


def get_mail() -> None:
    time.sleep(3)
    print("You get the mail")


def main() -> None:
    core1 = threading.Thread(target=get_mail)
    core1.start()

    # Pass arguments using `args=()` to avoid immediate execution
    core2 = threading.Thread(target=take_out_trash, args=("dustbin",))
    core2.start()

    core3 = threading.Thread(target=walk_dog, args=("tommy",))
    core3.start()

    # Wait for threads to finish
    core1.join()
    core2.join()
    core3.join()


if __name__ == "__main__":
    main()
