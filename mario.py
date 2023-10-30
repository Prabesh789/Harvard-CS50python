# print mario # column
def main():

    print_column(3)


# abstract : here main function does not need to know the underline implementation of print_column function has changed


def print_column(height):
    # for _ in range(height):
    #     print("#")
    print("#\n" * height, end="")


main()


# print mario ? row
def main():
    print_row(4)


def print_row(width):
    print("?" * width)


main()
"""
let's solve mario square

###
###
###

"""


# --------------------------------------
def main():
    print_square(3)


def print_square(size):
    # for each row in square
    for i in range(size):
        # for each brick in row
        for j in range(size):
            #  print brick
            print("#", end="")
        # \n
        print()


main()


def main():
    print_square(3)


def print_square(size):
    for _ in range(size):
        print_row(size)
        # print("#" * size)


def print_row(width):
    print("#" * width)


main()
