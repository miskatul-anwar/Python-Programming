import os
import send2trash as tput


def delete_file(name):
    if name in os.listdir():
        # if name.endswith(".txt"):
        os.unlink(name)


def trash_file(name):
    if name in os.listdir():
        # if name.endswith(".txt"):
        tput.send2trash(name)


def main():
    name = str(input("Delete file: "))
    conf = input("Parmanent delete (Y/N)? ")
    if conf == "Y" or conf == "y":
        delete_file(name)
    else:
        trash_file(name)
    if name in os.listdir():
        print("File Not Deleted")
    else:
        print("File Deleted")


if __name__ == "__main__":
    main()
