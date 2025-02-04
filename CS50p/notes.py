answer = input("what is the answer to the Great Question of Life, the Universe and Everyhing ?")

match answer.lower().strip():
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")


x, y, z = expression.split(" ")
# will assign 1 to x, + to y, and 1 to z.


print(f"hello, {name}")

z = round(x / y, 2)  same as below
print(f"{z:.2f}")

if s is a str, you could print each of its characters, one at a time, with code like:

for c in s:
    print(c, end="")



De Morgan's Law. (not A) and (not B) is equivalent to not (A or B), and (not A) or (not B) is equivalent to not (A and B).

print(f"x is {x}")
Notice that by including the f, we tell Python to interpolate what is in the curly braces as the value of x.

 For best practice, we should only try the fewest lines of code possible that we are concerned could fail.

round(2.6) = 3
int(2.6) = 2

except EOFError:  catches control d
    break
total = 6.0
"{0:.2f}".format(total)

print(f"{9:02}")
09


print(f"${total_price:,.4f}")
converts "33445.4545" to $33,445.4545
https://docs.python.org/3/library/string.html#formatspec

str.rindex() finds the highest index

pass if not(0<=x<=1) else break
