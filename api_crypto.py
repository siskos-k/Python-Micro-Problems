import tkinter as tk
import requests

class CryptoPriceTracker:
    def __init__(self, master):
        self.master = master
        self.master.title('Crypto Price Tracker')

        self.label = tk.Label(self.master, text='Crypto Prices:')
        self.label.grid(row=0, column=0)

        self.btc_label = tk.Label(self.master, text='BTC:', font=('Helvetica', 14))
        self.btc_label.grid(row=1, column=0)

        self.btc_price = tk.Label(self.master, text='', font=('Helvetica', 14))
        self.btc_price.grid(row=1, column=1)

        self.eth_label = tk.Label(self.master, text='ETH:', font=('Helvetica', 14))
        self.eth_label.grid(row=2, column=0)

        self.eth_price = tk.Label(self.master, text='', font=('Helvetica', 14))
        self.eth_price.grid(row=2, column=1)

        self.doge_label = tk.Label(self.master, text='DOGE:', font=('Helvetica', 14))
        self.doge_label.grid(row=3, column=0)

        self.doge_price = tk.Label(self.master, text='', font=('Helvetica', 14))
        self.doge_price.grid(row=3, column=1)

        self.update_prices()

    def update_prices(self):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin&vs_currencies=usd')
        data = response.json()

        self.btc_price['text'] = f'${data["bitcoin"]["usd"]}'
        self.eth_price['text'] = f'${data["ethereum"]["usd"]}'
        self.doge_price['text'] = f'${data["dogecoin"]["usd"]}'

        self.master.after(5000, self.update_prices)

root = tk.Tk()
tracker = CryptoPriceTracker(root)
root.mainloop()
