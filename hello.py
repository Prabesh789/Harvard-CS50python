#Ask user for their name.
# Strings
name = input("What's your name? ").strip().title()
first, last = name.split(" ")
# say hello to user
print(f"Hello, {first}")
