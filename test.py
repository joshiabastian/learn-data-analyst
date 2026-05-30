import requests

base_url = "https://api.frankfurter.dev/v1"

date = input(
    "Please enter the date (in the format 'yyyy-mm-dd'), or type 'latest' if you are interested in the data for \
the most recent available date'):"
)
base = input("Convert from (currency): ")
curr = input("Convert to (currency): ")
amt = float(input("How much {} would you like to convert?: ".format(base)))

url = base_url + "/" + date + "?base=" + base + "&symbols=" + curr
response = requests.get(url)

if response.ok is False:
    print("\nError {}".format(response.status_code))
    print(response.json()["error"])
else:
    data = response.json()
    rate = data["rates"][curr]

    result = amt * rate

    print(
        "\n{0}{1} was equal to {2}{3}, based on the exchange rate on {4}".format(
            base, amt, curr, result, data["date"]
        )
    )
