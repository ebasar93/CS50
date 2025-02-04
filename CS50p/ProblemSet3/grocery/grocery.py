shop_list = {}

while True:
    try:
        x = input().upper()
    except EOFError:
        break
    except:
        pass
    else:
        if x not in shop_list:
            shop_list[x] = 1
        else:
            shop_list[x] += 1

for i in shop_list:
    print(shop_list[i],i)
