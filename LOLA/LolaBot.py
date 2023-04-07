## Lola is a beginner trading bot ##



from turtle import clear
import requests ## importing the requests library for the API call
import pandas as pd ## importing the panda's module for data structuring code
from datetime import datetime as dt ## importing Datetime to use date formats in API calls
import pandas_datareader.data as pdr #importing pandas web data reader
from matplotlib import pyplot as plt ## importing pyplot from the matplotlib library


##Set up variables
start_date = dt(2009,7,10) ## using datetime function to convert date to time
end_date = dt(2022,7,10)
symbols = ['QQQ'] ##symbol to look at
cash = 10000

stock_data = pdr.get_data_yahoo(symbols,start_date,end_date) #calling yahoo api to get stock level data on symbol list
adj_close = stock_data['Adj Close']

##setup/function

def stock_return():
    data = pd.DataFrame()
    for i in range(len(adj_close)):
        stock_return=(((adj_close.iat[i,0])-adj_close.iat[0,0])/adj_close.iat[0,0])*100
        df1={'Date':adj_close.index[i],'Stock Return':stock_return}
        data = data.append(df1,ignore_index = True)  
    return data
def trade_bot(starting_cash):
    trade = 0
    B_S_FLAG = 'B'
    buy_level=0
    sell_level=0
    daily_return = 0.0
    cash_return = 0.0
    cash=starting_cash
    data = pd.DataFrame()
    for i in range(len(adj_close)):
        current_day = adj_close.iat[i,0]
        previous_day = adj_close.iat[i-1,0]
        if B_S_FLAG == "B": ##checks if we are currently looking to buy
            if current_day > previous_day: ##If today is > than yesterday we buy
                B_S_FLAG = "S"
                trade +=1
                buy_level = current_day
        elif B_S_FLAG == "S": ## checking if we are currently looking to sell
            if current_day<previous_day: ## if today is < than yesterday we sell
                B_S_FLAG = "B"
                trade+=1 
                sell_level = current_day
                daily_return = ((sell_level-buy_level)/buy_level)*100 ## calculates return from the level we bought at to where we sold at
                cash*=1+(daily_return/100) ## multiplying our cash amount by the return we recieved between the buy and sell level
        cash_return = ((cash-starting_cash)/starting_cash)*100
        df1={'Date':adj_close.index[i],'Cash':cash,'Price':current_day,'Buy/Sell':B_S_FLAG,'Buy Level':buy_level,'Return':daily_return,'Total Return':cash_return}
        data = data.append(df1,ignore_index = True)  
    return data
def graphing(bot):
    ##Graphing returns data
    stock_data=stock_return()
    fig = plt.figure()
    ax = fig.add_subplot(211)
    plt.xticks(rotation=25)
    ax.plot(bot['Date'],bot['Total Return'],color=('#93A17C'),marker='',markerfacecolor='k',linestyle='-',label = 'Total Return')
    ax.plot(bot['Date'],stock_data['Stock Return'],color=('#A4C1CD'),marker='',markerfacecolor='k',linestyle='-',label = symbols[0])
    plt.title('Returns Graph')
    plt.xlabel('Date')
    ax.set_ylabel('Percent Return')
    ax.legend(loc='upper left')

    ##Graphing cash data
    ax=plt.subplot(212)
    plt.xticks(rotation=25)
    plot1=ax.plot(bot['Date'],bot['Cash'],color=('#c898d4'),marker='',markerfacecolor='k',linestyle='-',label = 'Cash Value')
    ax2=ax.twinx()
    plot2=ax2.plot(bot['Date'],adj_close,color=('#524546'),marker='',markerfacecolor='k',linestyle='-',label = "Price")
    plt.title('Cash/Price Graph')
    plt.xlabel('Date')
    ax.set_ylabel('Cash Return')
    ax2.set_ylabel('Price')
    lns = plot1+plot2
    labs = [l.get_label() for l in lns]
    ax.legend(lns,labs,loc='upper left')
    plt.subplots_adjust(hspace = .5, bottom = .1)
    plt.show()

graphing(trade_bot(cash))




