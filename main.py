import yfinance as yf
import json
import time
import os
import sys

global data
data = {
    "Money": 0,
    "Stocks": [0,0,0,0,0,0,0],
    "BoughtAt": [0,0,0,0,0,0,0]
}



global companies
companies = ["MSFT","AAPL","TSLA","FB","NVDA","DIS","PYPL"]

global stockPrices 
stockPrices = [0,0,0,0,0,0,0,0]

global boughtAt
boughtAt = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]


#Setup the program by checking if data exists, if not create a new data file
def startup():
    global data
    path = os.getcwd() + '\data.json'
    
    if not os.path.exists(path):
        print("File not found, creating file")
        data = {
            "Money": 1000,
            "Stocks": [0,0,0,0,0,0,0],
            "BoughtAt": [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        }
        jsonString = json.dumps(data)
        file = open('data.json',"w")
        file.write(jsonString)
        file.close()  
    else:
        print("File found, loading data.")
        file = open('data.json','r')
        data = json.load(file)
        file.close()
    print("Fetching current prices")
    getStockInfo()
    




#Fill in the current prices for the companies in order
def getStockInfo():
    global stockPrices
    global companies
    for company in companies:
        ticker = yf.Ticker(company)
        data = ticker.history()
        price = (data.tail(1)['Close'].iloc[0])
        price = round(price,2)
        index = companies.index(company)
        stockPrices[index] = price
        

#displays current stock info
def displayStocks():
    global data
    global companies
    global stockPrices
    for company in companies:
        index = companies.index(company)
        price = stockPrices[index]
        price = round(price,2)
        stockHeld = data["Stocks"][index]
        print(company + "   -   " + str(price) + "      Held: " + str(stockHeld))


#Purchase stock at the current price.
def purchaseStock(spent,company):
    global data
    global companies
    global stockPrices
    index = companies.index(company)
    price = stockPrices[index]
    stockGained = (spent/price)
    data["Stocks"][index] += stockGained
    data["Money"] -= spent
    data["BoughtAt"][index] = price
    print("Success, " + str(stockGained) + " of " + company + " purchased")



#Sell stock at the current price
def sellStock(amount, company):
    global data
    global companies
    global stockPrices
    index = companies.index(company)
    price = stockPrices[index]
    moneyGained = (price*amount)
    moneyGained = round(moneyGained,2)
    data["Money"] += moneyGained
    data["Stocks"][index] -= amount
    if data["Stocks"][index] == 0:
        data["BoughtAt"][index] = 0
    print("$" + str(moneyGained) + " made from " + str(amount) + " shares of " + company + " sold")
    

#Check if a minute has passed since the inputted time
def checkUpdate(oldTime):
    return time.time() - oldTime >= 60


def displayUserData():
    global data
    print("Money available: " + str(data["Money"]))



#Allows user to buy and sell stock
def userInput():
    global data
    global companies
    global stockPrices
    choice = input("Buy/Sell/Exit?:\n")
    if choice.lower() == "buy":
        stockToBuy = input("Which stock:    ")
        if stockToBuy in companies:
            moneySpent = input("How much money to use:  ")
            moneySpent = float(moneySpent)
            if moneySpent <= data["Money"]:
                purchaseStock(moneySpent,stockToBuy)
            else:
                print("Error, not enough money")
        else:
            print("Error, company not found")
    elif choice.lower() == "sell":
        stockToSell = input("Which stock:   ")
        if stockToSell in companies:
            stockHeld = data["Stocks"][companies.index(stockToSell)]
            if stockHeld > 0:
                amountToSell = input("How much to sell (Amount of stock/all)?:    ")
                if amountToSell.lower() == "all":
                    sellStock(stockHeld,stockToSell)
                else:
                    amountToSell = float(amountToSell)
                    if amountToSell <= stockHeld and amountToSell > 0:
                        sellStock(amountToSell,stockToSell)
                    else:
                        print("Error, invalid input")
            else:
                print("Error, no stock held in that company")        

    elif choice.lower() == "exit":
        shutDown()
    else:
        print("Error, invalid command")


#Saves user data
def shutDown():
    global data
    file = open('data.json','w')
    json.dump(data,file)
    file.close()
    print("Data saved")
    input("Press enter to exit")
    sys.exit()


#Main loop
def main():
    startup()
    oldTime = time.time()
    running = True
    while running:
        displayStocks()
        if checkUpdate(oldTime):
            getStockInfo()
        displayUserData()
        userInput()
            






if __name__ == '__main__':
    main()