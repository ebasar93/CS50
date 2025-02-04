menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        x = input("Item: ").title()
        total += float(menu[x])
    except EOFError:
        break
    except:
        pass
    else:
        print("Total: $" + "{0:.2f}".format(total) )
