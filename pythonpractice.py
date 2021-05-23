from fmp_python.fmp import FMP

import requests
import pandas as pd
import matplotlib.pyplot as plt


fmp = FMP(api_key='16dd1313b4c661c42a11f4360829f718')
quote = fmp.get_quote('AAL')
print(quote)

companies = ['AAPL','FB','GOOG','F','TSLA']
listofdf = []
for item in companies:
    print(item)
    histprices = requests.get(f"https://financialmodelingprep.com/api/v3/historical-price-full/{item}?serietype=line&apikey=16dd1313b4c661c42a11f4360829f718")
    histprices = histprices.json()

#Parse the API response and select only last 600 days of prices
    histprices = histprices['historical'][-600:]

#Convert from dict to pandas datafram

    histpricesdf = pd.DataFrame.from_dict(histprices)

#rename column
    histpricesdf = histpricesdf.rename({'close': item}, axis=1)
    
#append all dfs to list
    listofdf.append(histpricesdf)

#set index of each DataFrame by common column before concatinatinghtem
dfs = [df.set_index('date') for df in listofdf]

histpriceconcat = pd.concat(dfs,axis=1)

#divide all dataframe by first line of data to enable comparison
histpriceconcat = histpriceconcat/histpriceconcat.iloc[0]

for i, col in enumerate(histpriceconcat.columns):
    histpriceconcat[col].plot()

plt.title('Price Evolution Comparison')

plt.xticks(rotation=70)
plt.legend(histpriceconcat.columns)
plt.savefig('foo1.png', bbox_inches='tight')