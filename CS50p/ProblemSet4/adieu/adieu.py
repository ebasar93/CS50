import inflect

p = inflect.engine()
names = []
while True:
    try:
        x = input("Name: ").title()
        names.append(x)
    except EOFError:
        break

mylist = p.join(names)

print("Adieu, adieu, to " + mylist)
