def main():
    x = input("Fraction: ")
    percentage = convert(x)
    print( gauge(percentage))

def convert(fraction):
    x,y = fraction.split("/")
    # check if x and y are ints not str,floats
    try:
        float(x + y) != int(x + y)
    except ValueError :
        raise(ValueError)

    x,y = int(x), int(y)
    if x > y :
         raise ValueError
    return round ((x/y) * 100)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return str(round(percentage)) + "%"


if __name__ == "__main__":
    main()
