class item:

    def __init__(self, name, price, amount, catagory="none"):
        self.name = name
        self.price = price
        self.amount = amount
        self.catagory = catagory

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getAmount(self):
        return self.amount

    def setAmount(self, amount):
        self.amount = amount

    def addAmount(self, amount):
        self.amount += amount

    def getCatagory(self):
        return self.catagory

    def setCatagory(self, cata):
        self.catagory = cata
