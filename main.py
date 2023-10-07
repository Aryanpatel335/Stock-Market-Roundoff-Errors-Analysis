import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import math

ticker_sym = "^GSPC" # want to fetch the S and P 500 Index

#start-date and end-date difference from today to day before
start_date = '2009-03-01' # beginning of Bull Market 
end_date = '2020-02-20' # end of Bull Market (Second longest in history)

# this is to collect the data from the yfinance library 
stock_data = yf.download(ticker_sym, start=start_date, end=end_date)

# converting data into pandas dataframe
df = pd.DataFrame(stock_data)

pctChange_adjClose = list(df['Adj Close'].pct_change()*100)
pctChange_adjClose.pop(0) # pop initial value NaN percent change

# this array will hold truncated values chopped to 2 decimal places. It will not be rounded
# example 0.1256 --> 0.12 
truncated_pctChange = []

def truncate(number, decimal_places):
    if number < 0:
        number = number * -1
        multiplier = 10 ** decimal_places
        truncated_number = math.floor(number * multiplier) / multiplier
        return truncated_number * -1
    else: 
        multiplier = 10 ** decimal_places
        truncated_number = math.floor(number * multiplier) / multiplier
        return truncated_number


for i in pctChange_adjClose:
    truncated_pctChange.append(truncate(i,2))

truncated_adjClose = []

# this is the first value in the dataframe
truncated_adjClose.append(truncate(df['Adj Close'].iloc[0],2))

for i,j in enumerate(truncated_pctChange):
    # calculate next days value from previous day based on percent change
    chopped_val = truncated_adjClose[i] * (1 + (j/100))
    # truncate to 2 decimal places
    truncated_adjClose.append(truncate(chopped_val,2))

#sizing the plot
plt.figure(figsize=(18,9))

df['Truncated Adj Close'] =  truncated_adjClose

# print(df['Truncated Vals'], df['Adj Close'])

plt.plot(df.index, df['Adj Close'], label='Adjusted Close for S and P 500 2008-2020 Bull Market')
plt.plot(df.index, df['Truncated Adj Close'], label='Truncated Adjusted Close for S and P 500 2008-2020 Bull Market')

# basic labelling of the graph
plt.title('S and P 500 Adjusted Closing Price vs Truncated Adjusted Closing Price')

plt.xlabel('Date')
plt.ylabel('Adj Closing Prices')
plt.legend()
plt.grid(True)
plt.show()
