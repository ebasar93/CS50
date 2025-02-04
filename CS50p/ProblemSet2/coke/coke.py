amount_due = 50
while amount_due > 0:
    print("Amount Due: " + str(amount_due) )
    x = input("Insert Coin: ")
    match x :
        case "5" | "25" | "10":
            amount_due -= int(x)
            if amount_due <= 0:
                print("Change Owed: " + str(abs(amount_due)))
                break
        case _:
            continue

