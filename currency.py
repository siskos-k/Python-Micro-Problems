import requests
import json

def get_exchange_rates(api_key):
    url = f'https://api.exchangeratesapi.io/latest?base=USD&symbols=EUR,AUD&api_key={api_key}'
    response = requests.get(url)
    data = json.loads(response.text)
    return data['rates']

def convert_currency(initial_currency, amount, rates):
    for currency, rate in rates.items():
        if currency != initial_currency:
            equivalent_amount = amount * rate
            print(f'{amount} {initial_currency} is equal to {equivalent_amount:.2f} {currency}')

def main():
    api_key = 'your_api_key_here'
    rates = get_exchange_rates(api_key)

    while True:
        initial_currency = input('Enter the initial currency (USD, EUR, AUD): ').upper()
        while initial_currency not in rates:
            initial_currency = input('Invalid currency. Please enter USD, EUR or AUD: ').upper()

        amount = float(input('Enter the amount: '))

        convert_currency(initial_currency, amount, rates)

        play_again = input('Do you want to convert again? (yes/no): ').lower()
        if play_again != 'yes':
            break

if __name__ == '__main__':
    main()
