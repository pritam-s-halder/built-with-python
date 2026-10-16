account = {
    "name": "rem.minamoto",
    "balance": 25000,
    "pin": "2222",
    "type": "savings account"
}

MAX_PIN_ATTEMPTS = 3

def read_amount():
    raw = input("Enter your amount: ")
    try:
        return int(raw)
    except ValueError:
        print("Invalid amount")
        return None

print("----MINI ATM----")

authenticated = False
for attempt in range(MAX_PIN_ATTEMPTS):
    pin = input("Enter your pin: ")
    if pin == account["pin"]:
        authenticated = True
        break
    print(f"Invalid PIN ({MAX_PIN_ATTEMPTS - attempt - 1} attempts left)")

if authenticated:
    while True:
        print("\n**** ATM MENU ****")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Account Details")
        print("5. EXIT")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("YOUR BALANCE IS:", account["balance"])

        elif choice == "2":
            amount = read_amount()
            if amount is None:
                continue

            if amount > 0:
                account["balance"] += amount
                print("Money deposited successfully!")
                print("NEW BALANCE:", account["balance"])
            else:
                print("Invalid amount")

        elif choice == "3":
            amount = read_amount()
            if amount is None:
                continue

            if amount <= 0:
                print("Invalid amount")
            elif amount > account["balance"]:
                print("Insufficient money")
            else:
                account["balance"] -= amount
                print("COLLECT YOUR CASH")
                print("NEW BALANCE:", account["balance"])

        elif choice == "4":
            print("\nACCOUNT NAME:", account["name"])
            print("ACCOUNT BALANCE:", account["balance"])
            print("ACCOUNT TYPE:", account["type"])

        elif choice == "5":
            print("Closing program....")
            break

        else:
            print("Invalid choice")

else:
    print("Access denied")
