s = input("camelCase: ")
for i in s:
    if i.isupper():
        n = "_" + i.lower()
        s = s.replace(i,n)
print("snake_case: " + s)
