months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    x = input("Date: ")
    if "," not in x and "/" not in x:
        continue
    if x[0].isnumeric():
        a = x.split("/")
        if int(a[0]) > 12 or int(a[1])> 31:
            continue
        print(f'{int(a[2]):02}-{int(a[0]):02}-{int(a[1]):02}')
        break
    else:
        x = x.replace(',','')
        a = x.split(" ")
        if int(a[1]) > 31:
            continue
        else:
            a[0] = str(months.index(a[0])+1)
            print(f'{int(a[2]):02}-{int(a[0]):02}-{int(a[1]):02}')
            break

