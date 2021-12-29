class Atm:

    def __init__(self, pin, cardNum, balance):
        self.pin = pin
        self.cardNum = cardNum
        self.balance = balance

    def createCard(self):
        print("This process is for card creation")

    def checkBalance(self, balance):
        print("Your current card balance is", balance, "rupees")

    def withdraw(self, cardNum, pin):
        print("Withdrawl coming soon!!")

cardA = Atm(1234, 1, 1000)

cardA.checkBalance(1000)