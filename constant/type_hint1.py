def meow(n: int) -> str:
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
'''
here in line 1 " -> str " is the type hint for return type for meow function 
'''
