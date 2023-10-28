# conditionals with match
name = input("What's your name? ")

match name:
    case "A" | "B" | "C":
        print("abc")
    case "D":
        print("d")
    case _:
        print("Who?")
