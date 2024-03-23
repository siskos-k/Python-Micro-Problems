import tkinter as tk
import requests
import json

def convert_currency():
    initial_currency = initial_currency_entry.get()
    amount = amount_entry.get()
    rates = get_exchange_rates('your_api_key_here')

    for currency, rate in rates.items():
        if currency != initial_currency:
            equivalent_amount = amount * rate
            print(f'{amount} {initial_currency} is equal to {equivalent_amount:.2f} {currency}')

def get_exchange_rates(api_key):
    url = f'https://openexchangerates.org/api/latest.json?app_id={api_key}'
    response = requests.get(url)
    data = json.loads(response.text)
    rates = data['rates']
    return rates

window = tk.Tk()

initial_currency_label = tk.Label(window, text="Initial Currency:")
initial_currency_label.pack()

initial_currency_entry = tk.Entry(window)
initial_currency_entry.pack()

amount_label = tk.Label(window, text="Amount:")
amount_label.pack()

amount_entry = tk.Entry(window)
amount_entry.pack()

convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.pack()

window.mainloop()
