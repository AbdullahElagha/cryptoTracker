import csv
import sys
import showWallet
import importWallet


walletDict = {}  # dictionary to store coin names for wallets that have been created
priceDict = {}  # dictionary to story prices for coins
divider = ("-" * 50)
BTC = 11000


# function to calcluate dollar value against BTC on given date


class Portfolio:
    """common class for cryptocurrency portfolio tracking """

    def __init__(self, nameFirst, units, priceBTC, timeStamp):
        self.nameFirst = nameFirst  # cryptocurrency name
        self.units = units  # number of units per coin
        self.priceBTC = priceBTC  # initial purchase price BTC
        self.price = (self.priceBTC * BTC)  # convert price from BTC to USD
        self.totalSale = units * self.price  # purchase total BTC
        self.walletValue = self.totalSale  # total wallet value BTC
        self.name = self.nameFirst[4:]
        self.transactionList = [(self.name, units, self.price, timeStamp)]  # create list to track transactions
        print(
            "A new wallet was created for {} with {} units deposited at ${} for a total of ${}".format(self.name, units,
                                                                                                       self.price,
                                                                                                       self.totalSale))
        print(divider)

    # function to make new buy into crypto wallet
    def buy(self, amount, currentPriceBTC):
        currentPrice = (currentPriceBTC * BTC)  # convert price from BTC to USD
        self.units += amount  # update wallet units
        self.totalSale = (amount * currentPrice)  # calaculate total buy USD
        self.walletValue += self.totalSale  # update wallet USD value
        self.transactionList.append((self.name, self.units, self.totalSale))  # update the trasnaction list
        print("{} deposit:".format(self.name))
        print(
            "{0:.8f} units deposited at ${1:.2f} for a total of ${2:.2f}".format(amount, currentPrice, self.totalSale))
        print("Total units of {}: {} units".format(self.name, self.units))
        print(divider)

    # function to view transaction list
    def showTransactions(self):
        for transaction in self.transactionList:
            print(transaction)
        print(divider)


# function to show the current contents of a particular wallet



def welcome():  # welcome screen

    print("Welcome to Cryptracker v1. Please choose from the following options")
    print("1. Import wallet from CSV")
    print("2. Manually enter wallet or transaction")
    print("3. Go to main page")
    print("4. Exit")

    welcomeInput = input()

    if welcomeInput == "1":
        importFromCSV()  #
    elif welcomeInput == "2":
        print("this functionality is not yet complete")
    elif welcomeInput == "3":
        mainPage()
    elif welcomeInput == "4":
        sys.exit("Good bye")
    else:
        print(" '{}' is not a valid entry".format(welcomeInput))
        welcome()

    mainPage()


def mainPage():
    print("this is the main page ")
    print("1. view wallet")
    print("2. Import Updated Prices")
    print("3. blankk")
    print("4. blankkk")
    print("5. Exit")
    print(divider)
    mainPageInput = input()

    if mainPageInput == "1":
        print("Here is a list of wallets currently in this tracker")
        for key, value in walletDict.items():
            print(key)
        print("Which wallet would you like to view?")
        walletQuery = input()
        print(walletQuery)
        if walletQuery in walletDict:
            walletQuery = walletDict[walletQuery]
            showWallet.py(walletQuery)
            mainPage()
        else:
            print("Invalid entry, there is no wallet called {}".format(walletQuery))
            mainPage()

    elif mainPageInput == "2":
        print("Uploading updated price list")
        updatePrices()
    elif mainPageInput == "4":
        sys.exit("Good bye")


def importFromCSV():
    z = "bittrexPortfolio.csv"
    tester = importWallet(z)


def manualEntry():
    print("lmao")


def updatePrices():
    testList = []
    x = y = 0
    priceCSV = "currentPrices.csv"
    with open(priceCSV, newline='') as csvfile:
        newPrices = csv.reader(csvfile, delimiter=',')
        for rows in newPrices:
            testList.append(rows)
        for row in testList:
            coinNameX = (testList[x][y])
            coinPriceX = (testList[x][y + 1])
            priceDict[coinNameX] = coinPriceX
            x = x + 1
    print(priceDict)
    mainPage()


welcome()



# MAIN


# bittrexCSV = []	# list to store each row from CSV as a list i.e. list of lists 
# bittrexSellOrders = [] # list for all sell order 
# bittrexBuyOrders = [] # list for all buy orders 
# walletDict = {}	# dictionary to store coin names for wallets that have been created

# # function to open CSV and load into list 
# with open('bittrexPortfolio.csv', newline='') as csvfile:
# 	bittrex = csv.reader(csvfile, delimiter=',')
# 	for rows in bittrex:
# 		bittrexCSV.append(rows)

# for row in bittrexCSV:
# 	print(row)

# print(Portfolio.divider)

# y = 0
# x = 0	

# # iterate through the individual lists 
# for row in bittrexCSV:
# 	# assign a variable to each item in the list 
# 	thisDate = (bittrexCSV[x][y])
# 	thisName = (bittrexCSV[x][y+1])
# 	thisUnits = float(bittrexCSV[x][y+2])	
# 	thisRate = float(bittrexCSV[x][y+3])	
# 	orderType = (bittrexCSV[x][y+4])
# 	thisNameFinal = thisName[4:]
# 	currentName = str(thisNameFinal)
# 	if orderType == " Buy":
# 		if currentName not in walletDict:
# 			bittrexBuyOrders.append(row)	# add to list of buy orders 
# 			print("the current name is: {} " .format(currentName))
# 			thisNameFinal = Portfolio(thisName, thisUnits, thisRate, thisDate)	# new wallet 
# 			walletDict[currentName] = thisNameFinal	# append new wallet to wallet dict
# 			thisNameFinal.showWallet()
# 		else:
# 			bittrexBuyOrders.append(row)
# 			walletDict[currentName].buy(thisUnits, thisRate)
# 	elif orderType == " Sell":	# for withdrawls 
# 		bittrexSellOrders.append(row)
# 		# walletDict[currentName].withdraw(transactionAmount)
# 	#print(thisNameFinal)

# 	x +=1	# iterate to next row 

# walletDict["OMG"].showWallet()
# walletDict["ARK"].showWallet()
