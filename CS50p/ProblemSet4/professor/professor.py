import random

def main():

    level = int(get_level())
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        lives = 3
        while lives > 0:
            s = input(f"{x} + {y} = ")
            try :
                int(s)
            except:
                lives -= 1
                print("EEE")
                pass
            else:
                if x + y == int(s):
                    score += 1
                    break
                else:
                    print("EEE")
                    lives -= 1
        if lives == 0:
            print(f"{x} + {y} = {x+y}  ")
    print(f"Score: {score}")
def get_level():
    while True:
        x = input("Level: ")
        try:
            x = int(x)
        except:
            pass
        else:
            if 0 < x < 4:
                return x


def generate_integer(level):
    if not(0 < level < 4):
        raise ValueError
    return random.randint(0 + 10*(level-1), 10**level - 1)

if __name__ == "__main__":
    main()
