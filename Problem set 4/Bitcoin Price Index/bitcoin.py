import requests
import sys

if len(sys.argv) == 2:
    try:
        ans = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin = bitcoin.json()
    bit = bitcoin["bpi"]["USD"]["rate_float"]
    total_amt = bit * ans
    print(f"${total_amt:,.4f}")

except requests.RequestException:
   print("RequestException")
   sys.exit(1)
