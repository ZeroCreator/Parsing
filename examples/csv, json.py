import csv

#with open("example.csv") as f:
#    reader = csv.reader(f)
#    for row in reader:
#        print(row)

#with open("example.tsv") as f:
#    reader = csv.reader(f, delimiter="\t")
#    for row in reader:
#        print(row)


# Запись
students = [
    ["Greg", "Dean", 70, 80, 90, "Good job, Greg"],
    ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
]

with open("example.csv", "a") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    #for student in students:
    #    writer.writerow(student)
    writer.writerows(students)