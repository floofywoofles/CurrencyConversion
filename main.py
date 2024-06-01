import sys
import argparse
import os
import orjson

JSON_FILE_PATH = os.path.join(f"{os.getcwd()}/data","usd.json")

with open(JSON_FILE_PATH, "r") as f:
    f_data = f.read()

json_data: dict = orjson.loads(f_data)

# print(json_data)

parser = argparse.ArgumentParser(
    prog="Currency Converter",
    description="A simple program to convert USD to any currency"
)
parser.add_argument(
    "amount",
    help="The amount to convert"
)

parser.add_argument(
    "currency",
    help="The currency to convert to"
)


args = parser.parse_args()

currency: str = args.currency
amount: str = args.amount

if currency.lower() not in json_data.keys():
    print(f"Invalid currency type: {currency}")
    sys.exit(1)

if not amount.isdigit():
    print(f"Amount provide is not a number: {amount}")
    sys.exit(1)

def get_conversion_rate(curr: str)->float:
    for key, value in json_data.items():
        if key == curr.lower():
            return value["rate"]

    return -1

conv_rate: float = get_conversion_rate(currency)
print(f"USD: {amount} | {currency}: {round(conv_rate*float(amount),2)}")