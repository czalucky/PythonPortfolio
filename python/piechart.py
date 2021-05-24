import matplotlib.pyplot as plt
import datetime as dt
from pandas_datareader import data as web

# x = [15, 25, 25, 30, 5]
# labels = ['Very Likely', 'Likely', 'Unsure', 'Unlikely', 'Very Unlikely']
colors = ['tab:blue', '#17174a', '#005d61','tab:cyan', '#7e2455']

tickers = ['AAPL','FB','GOOG','F','TSLA']
amounts = [12, 16, 12, 11, 7]
prices = []
total = []

for ticker in tickers:
    df = web.DataReader(ticker, 'yahoo', dt.datetime(2019,8,1), dt.datetime.now())
    price = df[-1:]['Close'][0]
    prices.append(price)
    index = prices.index(price)
    total.append(price * amounts[index])

fig, ax = plt.subplots(figsize=(15,8))
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.set_title('My Portfolio')
patches, texts, autotexts = ax.pie(total, labels=tickers, autopct='%1.1f%%', pctdistance=0.8, colors = colors)
[text.set_color('white') for text in autotexts]


#side info
ax.text(-2,1, 'PORTFOLIO OVERVIEW:', fontsize=24, color="#005d61", horizontalalignment='center', verticalalignment='center')
ax.text(-2,0.85, f'Total USD Amount: ${sum(total):.2f}', fontsize=18, color="green", horizontalalignment='center', verticalalignment='center')
counter = 0.15
for ticker in tickers:
    print(total[0])
    ax.text(-2, 0.85 - counter, f'{ticker}: ${total[tickers.index(ticker)]:.2f}', fontsize=16, color="black",
            horizontalalignment='center', verticalalignment='center')
    counter += 0.15

plt.savefig("//Users/cristinazalucky/Documents/GitHub/PythonProject/static/img/pieChart.png")