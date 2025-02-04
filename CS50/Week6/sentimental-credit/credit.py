from cs50 import get_int
n = get_int("Number: ")

def Luhn(n):
    if len(str(n)) > 16 or len(str(n)) < 13:
        return False
    sn = str(n)
    sum = 0
    for i in sn[-2::-2]:
        t =  int(i)*2
        if t > 9:
            t = str(t)
            sum+= int(t[0]) + int(t[1])
        else:
            sum += t
    for i in sn[-1::-2]:
        sum += int(i)
    if sum % 10 == 0:
        return True
    else:
        return False

def card_type(n):
    if Luhn(n) == True:
        if str(n)[0] == "4":
            print("VISA")
        elif str(n)[0:2] in ["34","37"]:
            print("AMEX")
        elif str(n)[0:2] in ["51","52","53","54","55"]:
            print("MASTERCARD")
        else:
            print("INVALID")

    else:
        print("INVALID")

card_type(n)



