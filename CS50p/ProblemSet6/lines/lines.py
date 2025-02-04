import sys
import os

if len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")

file_name = sys.argv[1]
name, ext = os.path.splitext(file_name)
if ext != ".py":
    sys.exit ("Not a Python file")
try:
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
        no = 0
        for line in lines:
            if not (line.lstrip().startswith('#') or line.isspace()):
                no += 1
        print(no)
except FileNotFoundError:
    print("File does not exist")



