#  Parity of a number refers to whether it contains an odd or even number of 1-bits

# x = int(input("What's x? "))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):

    # if n % 2 == 0:
    #    return True
    # else:
    #   return  False

    # improved
    # return True if n % 2 == 0 else False

    # improved
    return n % 2 == 0


main()
