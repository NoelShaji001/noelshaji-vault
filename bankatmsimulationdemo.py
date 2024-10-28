"""
Author:Noel Shaji
Date:28-10-2024
Descripotion:Write a program that stimulates simple bank ATM system.
"""
balance_amount=1000
while True:
    print("\n1.\tcheck balance")
    print("2.\tDeposit Money")
    print("3.\tWithdraw Money")
    print("4.\tExit")
    choice= int(input("Enter your choice:"))
    if choice == 1:
        print(f"The current balance $ {balance_amount}")
    elif choice == 2:
        deposit_amount=float(input("Enter your amount to be deposited:"))
        balance_amount=balance_amount+deposit_amount
        print(f"The Deposited amount ${deposit_amount} and The current balance ${balance_amount}")
    elif choice == 3:
        withdraw_amount=float(input("Enter your amount to be withdrawn:"))
        if (withdraw_amount > balance_amount):
            print("Insufficient Balance")
        else:
            balance_amount = balance_amount - withdraw_amount
            print(f"The Withdraw Amount ${withdraw_amount} and The current balance ${balance_amount}")
    if choice == 4:
        break
    else:
        print("Invalid Entry")
        










