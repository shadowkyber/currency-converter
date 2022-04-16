import requests


current = input("Starting currency: ").lower()  # currency code user is starting with

url = f"http://www.floatrates.com/daily/{current}.json"  # url of starting code
conversions = requests.get(url).json()  # dic of all conversion rates

usd_rate = conversions["usd"]["rate"]
eur_rate = conversions["eur"]["rate"]

while True:
    receive = input("Receiving currency: ").lower()  # currency code user what to turn into
    if not receive:  # if the user doesn't enter a receiving currency end program
        break
    money = float(input("Money: "))  # amount of money in starting currency
    
    print("Checking the cache...")
    if receive == "usd" or receive == "eur":
        print("Oh! It is in the cache!")
        if receive == "usd":
            rate = usd_rate
        else:
            rate = eur_rate
    else:
        print("Sorry, but it is not in the cache!")
        con = conversions[receive]
        rate = con["rate"]
    new = round(rate * money, 2)
    print(f"You received {new} {receive.upper()}.")
