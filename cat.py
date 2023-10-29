# loops
# lets print meow three times

# while
# i = 3
# while i != 0:
#     print("meow")
#     i = i - 1

# i = 0
# while i < 3:
#     print("meow")
#     i = i + 1

# i = 0
# while i < 3:
#     print("meow")
#     i += 1

# # for

# for i in range(3):
#     print("meow")

# for _ in range(3):  #pythonic
#     print("meow")

# print("meow\n" * 3, end="")  # pythonic

# while True:
#     n = int(input("What's n? "))
#     # if n < 0:
#     #     continue
#     # else:
#     #     break
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")


def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break  #return n
    return n


def meow(num):
    for _ in range(num):
        print("meow")


main()
