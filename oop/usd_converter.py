class USDConverter:

    def __init__(self):
        self.rates = {} # currency => rate for 1 USD


    def add_exchange_rate(self, currency, rate_for_1_usd):
        self.rates[currency.upper()] = rate_for_1_usd

    def display_exchange_rate(self, currency):
        currency = currency.upper()
        if currency not in self.rates:
            print(f"Sorry, we don't have exchange rate for currency {currency}")
            return
        print(f"=====================================================\n"
            f"1 USD = {self.rates[currency]} {currency}\n1 {currency} = {1/self.rates[currency]} USD\n"
              f"=====================================================")

    def convert(self, from_currency, to_currency, amount):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()
        if from_currency != 'USD' and to_currency != 'USD':
            print("We can only convert USD to other currency")
            return
        if from_currency == 'USD':
            result = amount*self.rates[to_currency]
            print(f"{amount} USD is {amount*self.rates[to_currency]} {to_currency}")

        else:
            result = amount*(1/self.rates[from_currency])
            print(f"{amount} {to_currency} is {amount*(1/self.rates[from_currency])} USD")
        return result


# creates USDConverter object
# add the following exchange rates:
# 1 USD = 3.16 NIS
# 1 USD = 113.73 Japanese yen
# 1 USD = 0.89 Euro
# display exchange rate from USD to Japanese yen (expected: 113.73)
# display exchange rate from Japanese yen to usd (expected: 0.008)
# display how many USD will I get for 30000 Yen
#     display how many euro will I get for 134 USD

if __name__ == '__main__':
    converter = USDConverter()
    converter.add_exchange_rate('nis', 3.16)
    converter.add_exchange_rate('yen', 113.73)
    converter.add_exchange_rate('eur', 0.89)
    converter.display_exchange_rate('yen')
    converter.convert('yen', 'usd', 30000)
    converter.convert('usd', 'eur', 134)