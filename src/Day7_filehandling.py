#Task 1:The Personal logger
print("TASK 1")
with open("journal.txt","a") as file:
    r=input("Your name and today's goal:")
    file.write("\n"+r)

with open("journal.txt","r") as file:
    r=file.read()
    print(r)
    
#Task 2: The CSV Student List
print("TASK 2")
import csv
with open("students.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        if row[2]=="Pass":
            print(row)

#Task 3:The Safe logger
print("TASK 3")
filename=input("Enter your file name:")
try:
    with open(filename) as file:
        file.read()
except FileNotFoundError:
    print("Oops! That file doesn't exist yet")