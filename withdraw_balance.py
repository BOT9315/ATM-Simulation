def withdraw_balance():
    import utils as np
    
    try:
        amount = float(input("Enter amount to withdraw from your account: "))
        if amount > 0:
            current_balance = sum(np.deposits) - sum(np.withdrawals)
            if amount > current_balance:
                print(f"Insufficient funds. Current balance: {current_balance}")
            else:
                np.withdrawals.append(amount)
                print("Withdrawal successful from your account.")
        else:
            print("Invalid amount. Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
