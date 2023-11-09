"""with open("file/students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
        # row = line.rstrip().split(",")
        # print(f"{row[0]} is in {row[1]}")
"""

# lets do it with declearing list and sort it with students name
students = []

with open("file/students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        # student = {}
        # student["name"] = name
        # student["house"] = house
        student = {"name": name, "house": house}
        students.append(student)

# get students names
'''def get_name(student):
    return student["name"]'''

for student in sorted(
        students,
        # key=get_name,
        key=lambda student: student["name"]):
    # this lambda function is equivalent with the get_name function. lamda also can take multiple paramaters
    print(f"{student['name']} is in {student['house']}")
