class Bank_Account:
    #class attributes
    bank_name = "Chase"
    account_type = "Checking"

    def __init__(self, name, number, balance):
        #instance attributes
        self.name = str(name)
        self.number = int(number)
        self.balance = int(balance)
        self.__amount1 = 0
        self.__amount2 = 0


    def deposit(self,x):
        self.__amount1 = x
    def withdraw(self, y):
        self.__amount2 = y

    def __str__(self):
        return self.name + "; your acount number is: " + str(self.number) + " and has a total balance of $ " + str(self.balance) + "  with a total deposits of $ " + str(self.__amount1) + " and a total withdraws for $ "  + str(self.__amount2) 
def main():
    Miriam = Bank_Account("Miriam", 613613, 30000)
    Miriam.deposit(200)
    Miriam.withdraw(100)
    print(Miriam)
