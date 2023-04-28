print("===========================================================")
print("Welcome to the banking system")
print("===========================================================")
name = input("Enter the username: \n")
balance = float(input("Enter the initial balance: \n"))
print("===========================================================")
print(f"Hello {name}, your initial balance is {balance}")
print("===========================================================")
print("What would you like to do?")
print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")
print("4. Exit")
print("===========================================================")

choice = input("Enter your choice: \n")

while choice != "4":
  if choice == "1":
      deposit_amount = float(input("Enter the amount to deposit: \n"))
      balance = balance + deposit_amount
      print(f"Your balance is {balance}")
      print("What would you like to do? \n")
      choice = input("Enter your choice: \n")
  elif choice == "2":
      withdraw_amount = float(input("Enter the amount to withdraw: \n"))
      if withdraw_amount > balance:
          print("You cannot withdraw more than your balance")
          print("What would you like to do? \n")
          choice = input("Enter your choice: \n")
      else:
        balance = balance - withdraw_amount
        print(f"Your balance is {balance}")
        print("What would you like to do? \n")
        choice = input("Enter your choice: \n")
  elif choice == "3":
      print(f"Your balance is {balance}")
      print("What would you like to do? \n")
      choice = input("Enter your choice: \n")
  else:
      print("Invalid choice")
      choice = input("Enter your choice: \n")

print("Thank you for using our banking system")
