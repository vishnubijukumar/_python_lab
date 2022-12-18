class bankAcc:
    name="";
    acc_no=0;
    acc_type="";
    acc_balance=0.0;
    def __init__(self):
        self.name=input("Enter the account holder name: ");
        self.acc_no=int(input("Enter account number: "));
        self.acc_type=input("Enter the account type: ");
        self.acc_balance=float(input("Enter the current account balance: "));
    def details(self):
        print(" Account Details: ");
        print("Name= ",self.name);
        print("Acc No= ",self.acc_no);
        print("Acc type= ",self.acc_type);
        print("Acc Balance = ",self.acc_balance);
    def deposit(self):
        print("Deposit");
        self.acc_balance=self.acc_balance+float(input("Enter the amount to be deposited: "));
        self.details();
    def withdraw(self):
        print("Withdraw");
        self.acc_balance=self.acc_balance-float(input("Enter the amount to withdraw: "));
        self.details();
ac=bankAcc();
ac.details();
ac.deposit();
ac.withdraw();
