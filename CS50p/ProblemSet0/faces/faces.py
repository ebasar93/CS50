def main():
    s = input()
    s = convert(s)
    print (s)

def convert(t):
    t = t.replace(":)","🙂")
    t = t.replace(":(", "🙁")
    return t

main()
