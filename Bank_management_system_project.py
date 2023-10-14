class Bank:
    def __init__(self) -> None:
         self.accounts = {}
         self.account_number = 100
         self.bank_balance = 0
         self.loan_enabled = False
         self.total_loan_amount = 0

    def create_account(self,name,email,address,account_type):
        account_number = self.account_number
        self.account_number  += 1
        self.accounts[account_number] = {
             'name' : name,
             'email' : email,
             'address' : address,
             'account_type': account_type,
             'balance' : 0,
             'transaction' : [],
             'loan_taken' : 0
        }
        return account_number

    def delete_account(self,account_number):
        if account_number in self.accounts :
            del self.accounts[account_number]
        else:
            print(f'\nAccount does not exist')
        
    def user_deposite(self,account_number,amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            self.accounts[account_number]['transaction'].append(f'Deposite tk : {amount}')
            self.bank_balance += amount
        else: 
            print('\nAccount does Not Exist')
    
    def user_withdraw(self,account_number,amount):
        if account_number in self.accounts:
            if amount > self.accounts[account_number]['balance']:
                print('\nWithdrawal amount exceeded.')
                if self.bank_balance < amount:
                    print("The bank is bankrupt.")
            else:
                self.accounts[account_number]['balance'] -= amount
                self.accounts[account_number]['transaction'].append(f'withdrew tk : {amount}')
                self.bank_balance -= amount

        else:
            print('\nAccount does Not exist.')
    
    def check_balance(self,account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]['balance']
        else:
            print("\nAccount does not exist.\nYou should first create an account.")
    
    def transaction_history(self,account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]['transaction']
        else:
            print("\nAccount does not exist.")

    def take_loan(self, account_number, loan_amount):
        if account_number in self.accounts:
            if self.loan_enabled and self.accounts[account_number]['loan_taken'] < 2:
                self.accounts[account_number]['loan_taken'] += 1
                self.accounts[account_number]['balance'] += loan_amount
                self.accounts[account_number]['transaction'].append(f'loan received : {loan_amount} tk')
                self.total_loan_amount += loan_amount
            elif self.accounts[account_number]['loan_taken'] >= 2:
                print(f"\nYou have already taken the maximum number of loans (2 times).")
            else:
                print("\nLoan feature is currently disabled.")
        else:
            print("\nAccount does not exist.\nYou should first Create an account.")

    def transfer_amount(self,sender_account_number, receive_account_number,amount):
        if sender_account_number in self.accounts and receive_account_number in self.accounts:
            if amount > self.accounts[sender_account_number]['balance']:
                print("\nInsufficient balance. You can't send money.")
            else: 
                self.accounts[sender_account_number]['balance'] -= amount
                self.accounts[receive_account_number]['balance'] += amount
                self.accounts[sender_account_number]['transaction'] .append(f'Transferred money: {amount} to account {receive_account_number}')
                self.accounts[receive_account_number]['transaction'].append(f'Received money: {amount} from account {receive_account_number}')
        else:
            print("\nAccount does not exist.\nyou should first create an account.")
    
    def admin_check_all_accounts(self):
        return self.accounts

    def admin_check_bank_balance(self):
        return self.bank_balance

    def admin_check_total_loan(self):
        return self.total_loan_amount

    def On_or_Off_loan_feature(self):
        self.loan_enabled = not self.loan_enabled 

class User:
    def __init__(self, bank, account_number):
        self.bank = bank
        self.account_number = account_number

    def deposite(self, amount):
        self.bank.user_deposite(self.account_number, amount)

    def withdraw(self, amount):
        self.bank.user_withdraw(self.account_number, amount)

    def check_balance(self):
        return self.bank.check_balance(self.account_number)

    def transaction_history(self):
        return self.bank.transaction_history(self.account_number)

    def take_loan(self, loan_amount):
        self.bank.take_loan(self.account_number, loan_amount)

    def transfer_amount(self, receiver_account_number, amount):
        self.bank.transfer_amount(self.account_number, receiver_account_number, amount)


class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        return self.bank.create_account(name, email, address, account_type)

    def delete_account(self, account_number):
        self.bank.delete_account(account_number)

    def check_all_accounts(self):
        return self.bank.admin_check_all_accounts()

    def check_bank_balance(self):
        return self.bank.admin_check_bank_balance()

    def check_total_loan(self):
        return self.bank.admin_check_total_loan()

    def On_or_Off_loan_feature(self):
        self.bank.On_or_Off_loan_feature()

bank = Bank()
admin = Admin(bank)
user1_account = admin.create_account('Rakibul islam','rakib@example.com','Rangpur','Admin')
user1 = User(bank, user1_account)
user1.deposite(5000)
user1.withdraw(2000)

user2_account = bank.create_account("Abdul jolil", "abdul@example.com", "mogbazar", "Current")
user2 = User(bank, user2_account)
user1.transfer_amount(user2_account, 1000)

admin.On_or_Off_loan_feature()
user1.take_loan(1000)

while True:

    print("\nBanking Management System Menu:\n")
    print("1>> Create an Account: ")
    print("2>> Delete an Account: ")
    print("3>> Deposit an Amount: ")
    print("4>> Withdraw an Amount: ")
    print("5>> Balance check: ")
    print("6>> Transfer an Amount: ")
    print("7>> Take Loan: ")
    print("8>> Account Transaction History: ")
    print("9>> See All User Accounts: ")
    print("10>> Check Total Loan Amount: ")
    print("11>> Turn On/Off Loan Feature: ")
    print("12>> Exit: ")
    print()
    option = input("Enter your choice: ")

    if option == '1':
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        account_type = input("Enter account type (Savings/Current): ")
        account_number = admin.create_account(name, email, address, account_type)
        print(f"\nAccount created with account number {account_number}")

    elif option == '2':

        account_number = int(input("Enter account number to delete: "))
        admin.delete_account(account_number)
        print(f"\nAccount {account_number} deleted")

    elif option == '3':
        account_number = int(input("Enter account number to deposit to: "))
        if account_number in bank.accounts:
            amount = int(input("Enter the deposit amount: "))
            user = User(bank, account_number)
            user.deposite(amount)  
            print(f"\nDeposited {amount} tk into account {account_number}")
        else:
            print("\nAccount does not exist. \nYou should first create an account.")


    elif option == '4':

        account_number = int(input("Enter account number to withdraw from: "))
        user = User(bank, account_number)
        balance = user.check_balance()
        if balance is not None:
            amount = int(input("Enter the withdrawal amount: "))
            if amount <= balance:   
                user.withdraw(amount)
                print(f"\nWithdrew {amount} tk from account {account_number}")
            else:
                print("\nWithdrawal amount exceeded.")
        else:
            print("\nAccount does not exist. \\nYou should first create an account.")

    elif option == '5':

        account_number = int(input("Enter account number to check balance: "))
        user = User(bank, account_number)
        balance = user.check_balance()
        if balance is not None:
            print(f"\nAccount {account_number} balance: {balance} tk")


    elif option == '6':
        sender_account = int(input("Enter sender account number: "))
        receiver_account = int(input("Enter receiver account number: "))
        if sender_account in bank.accounts and receiver_account in bank.accounts:
            amount = int(input("Enter the transfer amount: "))
            user = User(bank, sender_account)
            user.transfer_amount(receiver_account, amount)  
            print(f"\nTransferred {amount} tk from account {sender_account} to account {receiver_account}")
        else:
            print("\nAccounts do not exist. \nYou should first create the accounts.")

    elif option == '7':

        account_number = int(input("Enter your account number :"))
        user = User(bank,account_number)

        if account_number in bank.accounts:
            if bank.accounts[account_number]['loan_taken'] >= 2:
                print("\nYou have already taken the maximum number of loans (2 times).")
            else:
                loan_amount = int(input("Enter the loan amount: "))
                user.take_loan(loan_amount)
                if bank.loan_enabled:
                    print(f"Loan of {loan_amount} tk has been taken for account {account_number}")
        else:
            print("\nAccount does not exist. \nYou should first create an account.")
         
    elif option == '8':

        account_number = int(input("Enter account number to check transaction history: "))
        history = bank.transaction_history(account_number)
        if history is not None:
            print(f"\nTransaction history of account {account_number}: {', '.join(history)}")

    elif option == '9':

        accounts = admin.check_all_accounts()
        print("\nAll User Accounts:\n")
        for account_number, account_info in accounts.items():
            print(f"Account Number: {account_number}")
            print(f"Name: {account_info['name']}")
            print(f"Email: {account_info['email']}")
            print(f"Address: {account_info['address']}")
            print(f"Account Type: {account_info['account_type']}")
            print(f"Balance: {account_info['balance']} tk")
            print()

    elif option == '10':

        total_loan = admin.check_total_loan()
        print(f"\nTotal Loan Amount: {total_loan} tk")

    elif option == '11':
        admin.On_or_Off_loan_feature()
        loan_status = "enabled" if admin.bank.loan_enabled else "disabled"
        print(f"\nLoan feature is now {loan_status}")

    elif option == '12':

        print("\nExiting the system. Goodbye!")
        break
