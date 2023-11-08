# with open("names.txt", "r") as file:
#     names = file.readlines()

# for name in names:
#     print(f"Hello, {name.rstrip()}")
'''
this code also do the same as above in more pythonic way
with open("names.txt", "r") as file:
    for line in file:
        print(f"Hello, {line.rstrip}")
'''

# lets read the names from file and sorte them and print

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")

# This code is more compacted
# with open("names.txt") as file:
#     for line in sorted(file):
#         print("Hello,", line.rstrip())
