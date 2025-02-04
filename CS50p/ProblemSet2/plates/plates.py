def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")

    else:
        print("Invalid")


def is_valid(s):

    first_number = None
    last_char = None
    for c in s:
        if first_number == None:
            if c.isnumeric():
                first_number  = c
        if c.isalpha():
            last_char = c
    if first_number == "0":
        return False
    if s[0:2].isnumeric():
        return False
    if len(s) > 6 or len(s) <2:
        return False
    if s.isalnum() != True :
        return False
    if first_number != None:
        if s.index(first_number) < s.rindex(last_char):
            return False
    return True

main()
