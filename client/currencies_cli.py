import argparse
import json
import requests


# -u 'http://localhost:5000'


class CurrencyConverter():
    def __init__(self, url, input_currency, output_currency, amount):
        self.url = url
        self.input_currency = input_currency
        self.output_currency = output_currency
        self.amount = amount

    def convert_currency(self):
        r = requests.get("{}/currency_converter?from={}&to={}&amount={}"
                         .format(self.url, self.input_currency,
                                 self.output_currency, self.amount))
        if r.status_code == 200:
            return json.loads(r.content.decode("UTF8"))
        else:
            return 'Server is not reachable.'

    def convert_currency_all(self):
        r = requests.get("{}/currency_converter?from={}&amount={}"
                         .format(self.url, self.input_currency, self.amount))

        if r.status_code == 200:
            return json.loads(r.content.decode("UTF8"))
        else:
            return 'Server is not reachable.'


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="Url of the server.")
    parser.add_argument("-i", "--input_c", help="Input currency.")
    parser.add_argument("-o", "--output_c", help="Output currency.")
    parser.add_argument("-a", "--amount", help="Amount to convert.")
    return parser.parse_args()


def main():
    args = parse_args()
    c = CurrencyConverter(args.url, args.input_c, args.output_c, args.amount)
    if not args.output_c:
        print(json.dumps(c.convert_currency_all(), indent=4, sort_keys=True))
    else:
        print(json.dumps(c.convert_currency(), indent=4, sort_keys=True))


if __name__ == '__main__':
    main()
