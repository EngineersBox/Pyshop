from uuid import uuid4

class customer:

    def __init__(self, seshId=uuid4(), cart=[]):
        self.seshId = seshId
        self.cart = cart

    def getSeshId(self):
        return self.seshId

    def getCart(self):
        return self.cart

    def setCart(self, inven):
        self.cart = inven

    def addCart(self, item):
        self.cart.append(item)
