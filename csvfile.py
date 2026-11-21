import csv

with open("student.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print("{:<10} {:<10} {:<5} {:<10} {:<5}".format(*row))
