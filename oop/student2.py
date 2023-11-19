"""
Python allow us many possible types of data types to store the data. Also python allow us 
another general purpose tool that's going to allow us to create our own data types as well
and actually give them names and that terminology is a Class.

Class: it is kind of like a blueprint for pieces of data, object so to speak. We can define
and give them a name and when we use that mold or blueprint we get types of data that are 
designed exactly as we want so in short classes allow us to invent our own data types in Python 
and give them a name.

This is the primary feature of object oriented progamming to be able to create our own objects 
with own custom names.

Python classes allow for the creation of objects that can have both attributes (data) and methods (functions).
Attributes are defined within a class and can be accessed and modified by both the class and its objects.
"""


# new data type Student
class Student():
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__ == "__main__":
    main()

    #
    #
""" 
Here "student" in line 30 is an object of class Student or instantiation / instance of class Student.
An object that is created using a class is said to be an instance of that class. We will sometimes say
that the object belongs to the class. The variables that the object contains are called instance variables.
Here, in student.name and student.home in line 31 & 32 name & house are instance variables or attributes.
"""
