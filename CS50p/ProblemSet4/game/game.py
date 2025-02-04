import random

while True:
    try:
        x = int(input("Level: "))
        if x >= 1:
            break
    except:
        pass
    else:
        break

n = random.randint(1,x)

while True:
    a = int(input("Guess: "))
    if a == n:
        print("Just right!")
        break
    elif a > n:
        print("Too large!")
    else:
        print("Too small!")
