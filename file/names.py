# names = []

# for _ in range(3):
#     names.append(input("What's your name? "))

# for name in sorted(names):
#     print(f"Hello, {name}")
'''
Character

Meaning

'r':open for reading (default)

'w': open for writing, truncating the file first

'x': open for exclusive creation, failing if the file already exists

'a': open for writing, appending to the end of file if it exists

'b': binary mode

't': text mode (default)

'+': open for updating (reading and writing)
'''

# name = input("What's your name? ")
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# be more pythonic

name = input("What's yourr name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
