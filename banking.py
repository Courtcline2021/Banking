class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Hello! Welcome to the Deposit and Withdraw Menu")

    def deposit(self, ):
        amount = float(input("Enter amount Deposited: "))
        self.balance += amount
        display_bal = input("Would you like Account Balance \n Y/N?")
        if display_bal == "Y" or "y":
            print("\n Account Balance: ", self.balance) 
        else:
            print("\n Amount Deposited:", amount)  

    def withdraw(self):
        amount =(float(input("Enter amount to be Withdrawn: ")))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient Funds  ")     

    def display(self):
        print("\n Available Balance = ", self.balance) 


sam_account = Bank_Account()

sam_account.deposit()
sam_account.withdraw()
sam_account.display()