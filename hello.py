#Ask user for their name.
# Strings
# name = input("What's your name? ").strip().title()
# first, last = name.split(" ")
# # say hello to user
# print(f"Hello, {first}")


def main():
    name = input("What's your name? ")
    print(hello(name))


def hello(arg="world"):
    return f"Hello, {arg}"


if __name__ == "__main__":
    main()
