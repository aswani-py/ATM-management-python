class ATM:
    bank_name="SBI"
    def __init__(self,acc_no,acc_holder):
        self.acc_no=acc_no
        self.acc_holder=acc_holder
        self.balance=1000

    def display(self):
        print(f"Account Number:{self.acc_no}")
        print(f"Account Holder:{self.acc_holder}")
        print(f"Current Balance:{self.balance}")


    def balance_enquiry(self):
        print(f"Current Balance:{self.balance}")

    def deposit(self,amount):
        self.balance+=amount
        print(f"deposit amount:{amount}")
        print(f"current balance:{self.balance}")

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"withdrawel amount:{amount}")
            print(f"current balance:{self.balance}")
        else:
            print("insufficient balance")

obj1=ATM("1234xxxxxxx","Anu")

obj1.display()
print("=======================")
obj1.deposit(5000)
print("=======================")
obj1.withdraw(1000)
