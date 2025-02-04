while True :
    try:
        x = float(eval(input("Fraction: ")))
    except :
        pass
    elif not(0<=x<=1):
        pass
    else:
        if not (0<=x<=1):
            pass
        else:
            break

a = x * 100
if a >= 99:
    print("F")
elif a <=1:
    print("E")
else:
    print(str(round(a)) + "%")






