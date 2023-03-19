class Account:
    def __init__(self,title=None,Balance=0):
        self.title=title
        self.Balance=Balance
        
    def getBalance(self):
        return (self.Balance)
    
    def deposit(self,amount):
        self.Balance=self.Balance + amount      
     
    def withdrawal(self,amount):
        self.Balance=self.Balance - amount
    
        
class SavingsAccount(Account):
    def __init__(self,title,Balance,interestRate):
        super().__init__(title,Balance)
        self.interestRate=interestRate
        
    def interestAmount(self):
        interest=self.Balance*self.interestRate/100
        return(interest)

name,Balance,interestRate="Ashish",20000,5
acc=SavingsAccount(name,Balance,interestRate)
acc.deposit(100)
acc.withdrawal(500)
bal=acc.getBalance()
interest=acc.interestAmount()
print(f"Account Holder Name   : {acc.title}\nPrevious Account Balance is {Balance} $ \nCurrent Account Balance is {bal} $ \nInterest Amount is {interest} $")

#obj1=SavingsAccount("Ashish",5000,5)