with open("file/students.csv") as file:
    for line in sorted(file):
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
