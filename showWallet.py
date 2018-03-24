def showWallet(self):
    avgCost = self.walletValue / self.units  # calcluate average USD cost per coin
    print("{} wallet: ".format(self.name))
    print("{0:.8f} units | ${1:.2f} USD ".format(self.units, self.walletValue))
    foo = walletDict.get(self.name)
    # im just trying to buy time here but why
    print("Current Wallet value: ${} ".format(foo))
    print("Average cost per unit: ${0:.2f} USD".format(avgCost))
    print(divider)