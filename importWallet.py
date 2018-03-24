def importWallet(self):
    print("Input the name of the wallet: ")
    # csvName = input()
    csvName = "bittrexPortfolio.csv"
    bittrexCSV = []  # list to store each row from CSV as a list i.e. list of lists
    bittrexSellOrders = []  # list for all sell order
    bittrexBuyOrders = []  # list for all buy orders
    # walletDict = {}	# dictionary to store coin names for wallets that have been created

    # function to open CSV and load into list
    with open(csvName, newline='') as csvfile:
        bittrex = csv.reader(csvfile, delimiter=',')
        for rows in bittrex:
            bittrexCSV.append(rows)

    y = 0
    x = 0

    # iterate through the individual lists
    for row in bittrexCSV:
        # assign a variable to each item in the list
        thisDate = (bittrexCSV[x][y])
        thisName = (bittrexCSV[x][y + 1])
        thisUnits = float(bittrexCSV[x][y + 2])
        thisRate = float(bittrexCSV[x][y + 3])
        orderType = (bittrexCSV[x][y + 4])
        thisNameFinal = thisName[4:]  # reformat coin name
        currentName = str(thisNameFinal)  # convert name to string for dictionary
        if orderType == " Buy":
            if currentName not in walletDict:
                bittrexBuyOrders.append(row)  # add to list of buy orders
                thisNameFinal = Portfolio(thisName, thisUnits, thisRate, thisDate)  # new wallet
                walletDict[currentName] = thisNameFinal  # append new wallet to wallet dict
            else:
                bittrexBuyOrders.append(row)  # add to list of buy orders
                walletDict[currentName].buy(thisUnits, thisRate)  # new deposit
        elif orderType == " Sell":  # for withdrawls
            bittrexSellOrders.append(row)

        x += 1  # iterate to next row
    print("The wallet has been imported")
    print(divider)

