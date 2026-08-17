'''MINI ATM Machine'''
account = {
  "name" : "kai",
  "balance" : 500000,
  "pin" : "0110",
  "type" : "bussiness_account"
}

print("----MINI ATM----")

pin = input("Enter the pin : ")

if pin == account["pin"]:
  while True:
    print("****ATM MENU****")
    print("1. Check Balance :")
    print("2. Deposit Money :")
    print("3. Withdraw money :")
    print("4. Account Details :")
    print("5. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
      print("YOUR BALANCE IS ",account["balance"])

    elif choice == "2":
      amount = int(input("Enter your amount : "))

      if amount > 0:
        account["balance"] = account["balance"] + amount
        print("Money deposited successfully")
        print("NEW BALACNE",account["balance"])
      else:
        print("Invalid amount")

    elif choice == "3":
      amount = int(input("Enter your amount : "))

      if amount <= 0:
        print("Invalid amount")
      elif amount > account["balance"]:
        print("Insuffient amount")
      else:
        account["balance"] = account["balance"]-amount
        print("Collect YOUR CASH : ")
        print("NEW BALANCE",account["balance"])

    elif choice == "4":
      print("\nACCOUNT NAME",account["name"])
      print("ACCOUNT BALANCE",account["balance"])
      print("ACCOUNT TYPE",account["type"])

    elif choice == "5":
      print("---THANK YOU---")
      break
    else:
      print("INVALID CHOICE")

else:
  print("Invalid pin...")
  print("...Access Denied...")