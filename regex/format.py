import re

name = input("What's your name? ").strip()

# matches = re.search(r"^(.+), *(.+)$", name)
# if matches:
#     name = matches.group(2) + " " + matches.group(1)

# := walrus operator in python
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"Hello, {name}")