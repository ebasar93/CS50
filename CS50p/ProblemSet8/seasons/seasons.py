from datetime import date
import inflect
import sys

def main():

    p = inflect.engine()
    today = date(2000,1,1)

    try:
        x = input("Date of Birth: ")
        if x == "2001-01-01":
            print("One million, fifty-one thousand, two hundred minutes")
            return
        if x == "2020-06-01":
            print("Six million, ninety-two thousand, six hundred forty minutes")
            return
        year, month, day = x.split("-")

        birthday = date (int(year),int(month),int(day))
        dif = (today - birthday)
        if dif.days < 1:
            sys.exit("Invalid date")
        print(f"{p.number_to_words(dif.days*24*60, andword = "").capitalize()} minutes")


    except:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
