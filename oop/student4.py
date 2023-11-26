class Student():

    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # getter
    @property
    def house(self):
        return self._house

    # setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")

    return Student(name, house)


if __name__ == "__main__":
    main()
"""
Here we have get_student method outside student class which is the evidence of bad design, where related functions
should not be separated (practicing OOP) insted it should be encapsulated. i.e in Student class. Eg: in student5.py
"""
