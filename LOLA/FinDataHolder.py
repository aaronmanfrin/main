## Lola is a beginner trading bot ##



import requests ## importing the requests library for the API call
import pandas as pd ## importing the panda's module for data structuring code
from datetime import datetime as dt ## importing Datetime to use date formats in API calls
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols ## importing the nasdaq symbols funciton from the nasdaq trader module in the pandas datareader package
import pandas_datareader.data as pdr #importing pandas web data reader
from matplotlib import pyplot as plt ## importing pyplot from the matplotlib library
#

## nasdaq trader func
symbols = get_nasdaq_symbols()
#print(symbols)

## sp500 price func
start_date = dt(2019,1,1) ## using datetime function to convert date to time
end_date = dt(2019,2,1)
snp_data = pdr.DataReader('SP500', 'fred', start_date, end_date) ## calling sp500 level data between the dates set
snp_data['growth'] = snp_data['SP500'] - snp_data['SP500'].shift(1)## creating new column in the dataframe that represents the differenece between one date and next
#print(snp_data)


## Getting yahoo finance data

symbols = ['MSFT','AMZN','AAPL','GOOGL'] ##list of symbols to look at
stock_data = pdr.get_data_yahoo(symbols,start_date,end_date) #calling yahoo api to get stock level data on symbol list
#print(stock_data)

## grpahing yahoo data
x_axis = stock_data['Adj Close']
x_axis.plot(color=('pink','grey','blue','tan'),marker='X',markerfacecolor='k',linestyle='--')

plt.title('Stock Price Graph')
plt.xlabel('Date')
plt.ylabel('Price')

plt.legend(['MSFT','AMZN','AAPL','GOOGL'],loc='lower right')
plt.show()

## graphing random data using matplot lib

x=[2016,2017,2018,2019,2021,2022]
y1=[29,46,37,93,56,61]
y2=[87,41,77,48,95,12]


plt.plot(x,y1,color='pink',marker='o')
plt.plot(x,y2,color='gray',marker='o')
plt.title('Two Lines on One Graph')
plt.xlabel('Amazing x-axis')
plt.ylabel('Incredible Y-axis')
plt.legend(['Numers1','NUmber2'],loc='lower right')

#plt.show()

#API_response = request.get()



Lola = 1

print(str(Lola)+" is our return")
