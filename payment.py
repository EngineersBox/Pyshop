class payment:

    def __init__(self):
        self.cards = [] #USE EXTERNAL NOT LIST
        self.validIds = [] #USE EXTERNAL NOT LIST

    def auth(self, details, seshId):
        if details in self.cards and seshId in self.validIds:
            return True
        else:
            return False
