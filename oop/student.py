def main():

    # name, house = get_student()
    student = get_student()
    print(f"{student[0]} from {student[1]}")


# tuple: it's a another type of data in python wher a single var store multiple data, that is collection of valuse. i.e : x, y and it is ordered and immutable
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)


if __name__ == "__main__":
    main()
