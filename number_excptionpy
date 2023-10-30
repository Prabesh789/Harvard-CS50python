# runtine error
# exception

# ----- Scope of variable: The scope of a variable refers to the context in which that variable is visible/accessible to the Python interpreter

# ValueError : value of some variable, value of input in incorrect
# NameError : refers to your code


def main():
    number = get_int()
    print(f"X is {number}")


def get_int():
    while True:
        try:
            x = int(input("What's X? "))
        except ValueError:
            print("X is not an integer")
        # else:
        #     break
        else:
            return x  # here return is stronger than break => which can break and also return a value


main()


# improvised solution
def main():
    number = get_int("What's X? ")
    print(f"X is {number}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
