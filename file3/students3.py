import csv

name = input("what's your name? ")
home = input("Where's your home? ")

with open("file3/students3.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
