s = input("Input: ")
sik = s
# s.copy() = sik
vowels = ["a","e","i","o", "u"]
for c in s:
    if c.lower() in vowels:
        sik = sik.replace(c,"")
print("Output: " + sik)
