from forex_python.converter import CurrencyRates
import os
import json


class CurrencyManager():
    def __init__(self, input_c, output_c, amount):
        # check if null
        self.input_c = self.get_always_currency_code(input_c)
        self.output_c = self.get_always_currency_code(output_c)
        amount = float(amount)
        self.amount = amount
        self.c = CurrencyRates()

    def convert(self):
        output_dict = dict()
        if not self.input_c:
            output_dict["error"] = "Couldn't find the input curency."
            return self.parse_output(output_dict)
        if not self.output_c:
            output_dict["error"] = "Couldn't find the output curency."
            return self.parse_output(output_dict)

        result_amount = round(self.c.convert(
            self.input_c, self.output_c, self.amount), 2)
        output_dict[self.output_c] = result_amount

        return self.parse_output(output_dict)

    def convert_all(self):
        output_dict = dict()
        if not self.input_c:
            output_dict["error"] = "Couldn't find the input curency."
            return self.parse_output(output_dict)

        rates = self.c.get_rates(self.input_c)
        for output_c_key, value in rates.items():
            output_dict[output_c_key] = value * self.amount

        return self.parse_output(output_dict)

    def parse_output(self, output_dict):
        input_dict = {}
        input_dict["amount"] = self.amount
        input_dict["currency"] = self.input_c
        return {"input": input_dict, "output": output_dict}

    def get_always_currency_code(self, currency):
        import forex_python.converter
        file_path = os.path.dirname(
            os.path.abspath(forex_python.converter.__file__))
        with open(file_path + '/raw_data/currencies.json') as f:
            currencies_list = json.loads(f.read())
            for c in currencies_list:
                for key, value in c.items():
                    if currency == value:
                        return c["cc"]
