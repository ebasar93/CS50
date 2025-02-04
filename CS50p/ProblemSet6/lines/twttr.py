def main():
    s = input("Input: ")
    print("Output: " + shorten(s))


def shorten(word):
    vowels = ["a","e","i","o", "u"]
    sik = word
    for c in sik:
        if c.lower() in vowels:
            sik = sik.replace(c,"")
    return sik


if __name__ == "__main__":
    main()
