answer = input("what is the answer to the Great Question of Life, the Universe and Everyhing ?")

match answer.lower().strip():
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
