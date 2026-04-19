def atm():
    while True:
        print("\n======  WELCOM TO ATM MENU ======")
        print("1. Enter Display Balance")
        print("2. Enter Deposit Money")
        print("3. Enter Withdraw Money")
        print("4. Enter Statement/History")
        print("5. Enter Exit ATM")

        choice = input("Enter choice: ").strip()

        if not choice:
            print("No input entered. Please enter a number between 1 and 5.")
            continue

        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                from display_balance import display_balance
                display_balance()
            elif choice == 2:
                from deposit_balance import deposit_balance
                deposit_balance()
            elif choice == 3:
                from withdraw_balance import withdraw_balance
                withdraw_balance()
            elif choice == 4:
                from Statement_balance import statement
                statement()
            elif choice == 5:
                print("Thank you for using ATM!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

atm()