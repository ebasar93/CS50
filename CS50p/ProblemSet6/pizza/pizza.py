import sys
import csv
import os
from tabulate import tabulate

if len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")

file_name = sys.argv[1]
name, ext = os.path.splitext(file_name)
if ext != ".csv":
    sys.exit ("Not a csv file")

menu = []
with open(file_name) as file:
    reader = csv.reader(file)
    for row in reader:
        menu.append(row)
print(tabulate(menu,  headers="firstrow", tablefmt="grid"))

