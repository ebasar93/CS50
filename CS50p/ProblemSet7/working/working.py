import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        matches = re.search(r"(\d+):?(\d+)? (..) to (\d+):?(\d+)? (..)",s)

        if  matches.group(3) == "PM":
            t1 = eval(matches.group(1))+12
        else:
            t1 = matches.group(1)
        if matches.group(2) == None:
            t2 = "00"
        else:
            t2 = matches.group(2)
        if matches.group(6) == "PM":
            t3 = eval(matches.group(4))+12
        else:
            t3 = matches.group(4)

        if matches.group(5) == None:
            t4 = "00"
        else:
            t4 = matches.group(5)
        if int(t2) > 59 or int(t4)>59:
            raise ValueError



        return(f"{int(t1)%24:02}:{t2} to {int(t3)%24:02}:{t4}")
    except:
        sys.exit(ValueError)
if __name__ == "__main__":
    main()
