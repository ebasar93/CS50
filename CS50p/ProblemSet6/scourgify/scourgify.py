import sys
import os
import csv

if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")

file_name = sys.argv[1]
name, ext = os.path.splitext(file_name)
if ext != ".csv":
    sys.exit ("Not a csv file")
wr = open(sys.argv[2], "w")
wr.write("first,last,house\n")
with open(file_name,"r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        last,first = row['name'].split(',')
        wr.write(f"{first.strip()},{last},{row['house']}\n")

file.close()
