from cs50 import get_int

while True:
    h = get_int("Height: ")
    if h < 9 and h > 0:
        break

for i in range(h):
    for j in range(h-i-1):
        print(" ", end = "")
    for k in range(i+1):
        print("#", end = "" )
    print()
