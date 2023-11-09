import csv

students = []

with open("file1/students1.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student["name"]} is from {student["home"]}")
