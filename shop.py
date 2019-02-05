import customer, payment

class shop:

    def __init__(self, name, inven=[]):
        self.name = name
        self.inv = inven

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getInv(self):
        return self.inv

    def setInv(self, inven):
        self.inv = inven

    def appendInv(self, item):
        self.inv.append(item)

    def sortCat(self, cata):
        retArr = []
        for i in range(len(self.inv)):
            if self.inv[i].getCatagory() == cata:
                retArr.append(self.inv[i])
        return retArr

    def addToCart(self, cstmr, item, count):
        for i in self.inv:
            if i[0] == item and i[1] >= count:
                cstmr.addCart(item, amount)
            elif i[0] == item and i[1] < count:
                print("Not enough stock. Only " + i[1] + " left.")
                cstmr.addCart(item, i[1])
            else:
                pass

    def removeFromCart(self, cstmr, item, count):
        citem = 0
        remFlag = False
        for i in cstmr.cart:
            if i[0] == item and i[1] >= count:
                i[1] -= count
                if i[1] <= 0:
                    remFlag = True
                    citem = cstmr.cart.index(i)
            elif i[0] == item and i[1] < count:
                i[1] = 0
                remFlag = True
                citem = cstmr.cart.index(i)
        if remFlag == True:
            del cstmr.cart[citem]

    def checkout(self, cstmr):
        if len(cstmr.cart) > 0:
            total = 0
            for i in cstmr.cart:
                print(i[0].getName() + " x " + i[1])
                total += i[0].getPrice() * i[1]
                print("Total: " + total)
                cont = input("Proceed to payment? (y/n): ").lower()
                if cont == "y":
                    print()
                    cardNum = input("Card Number: ")
                    secCode = input("CVV: ")
                    Exp = input("Expiry date (dd/mm/yy): ")
                    details = [cardNum, secCode, Exp]
                    if payment.auth(details, cstmr.getSeshId()) == True:
                        print("Payment complete")
                    elif authed == False:
                        print("Card details are not valid")
                    else:
                        print("An error has occurred")
        else:
            print("Cart is empty")
