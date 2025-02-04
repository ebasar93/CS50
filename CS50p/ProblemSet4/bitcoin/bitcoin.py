import sys
import requests
import json

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

try:
    float(sys.argv[1])
except:
    sys.exit("command-line argument is not a number")


response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
#print(json.dumps(response.json(), indent=2))
o = response.json()
price = o["bpi"]["USD"]["rate"]
price = float(price.replace(",",""))
total_price = price * float(sys.argv[1])
print(f"${total_price:,.4f}")


