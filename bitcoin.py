import requests
import json
import sys
test = sys.argv[1]
if sys.argv.__len__()!= 2:
    sys.exit("Missing command-line argument")
elif not(sys.argv[1].replace(".", "").isnumeric()):
    sys.exit("Command-line argument is not a number")



try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    x = json.loads(r.text)
    rate = x["bpi"]["USD"]["rate"]
    num = float(rate.replace(",", ""))
    result = num * float(test)
    print(f"${result:,.4f}")
except requests.RequestException:
    ...
