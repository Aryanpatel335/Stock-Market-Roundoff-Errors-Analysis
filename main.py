import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import datetime

ticker_sym = "^GSPC" # want to fetch the S and P 500 Index

#start-date and end-date difference from today to day before
start_date = '2009-03-01' # beginning of Bull Market 
end_date = '2020-02-20' # end of Bull Market (Second longest in history)

# this is to collect the data from the yfinance library 
stock_data = yf.download(ticker_sym, start=start_date, end=end_date)

# converting data into pandas dataframe
df = pd.DataFrame(stock_data)

change_adjClose = list(df['Adj Close'].pct_change()*100)
# print(df['Adj Close'].pct_change()*100)
change_adjClose.pop(0)
truncated_percent_change = []
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


for i in change_adjClose:
    truncated_percent_change.append(truncate(i,2))

df['y'] = df['Adj Close']
# print(change_adjClose)    

#truncate to 2 decimal places

to_plot = []
to_plot.append(truncate(df['y'].iloc[0],2))
j=0
for i in truncated_percent_change:

    chopped_val = to_plot[j] * (1 + (i/100))
    j+=1
    to_plot.append(truncate(chopped_val,2))
# print(to_plot)
# print(change_adjClose)
#sizing the plot
plt.figure(figsize=(18,9))


 
to_list_plot = np.array(to_plot)
df['Truncated Vals'] =  to_list_plot.tolist()


plt.plot(df.index, df['Adj Close'], label='S and P 500 Closing Price 2008-2020 Bull Market')
plt.plot(df.index, df['Truncated Vals'], label='Truncated S and P 500 Adjusted Closing Price 2008-2020 Bull Market')


# basic labelling of the graph
plt.title('S and P 500 Adjusted Closing Price vs Truncated Adjusted Closing Price')

plt.xlabel('Date')
plt.ylabel('Adj Closing Price')
plt.legend()
plt.grid(True)
plt.show()

