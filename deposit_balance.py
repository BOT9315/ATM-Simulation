def deposit_balance():
    import utils as np
    try:
        
        amount = float(input("Enter amount to deposit into your account: "))
        if amount > 0:
            np.deposits.append(amount)
            print("Deposit successful in your account.")
        else:
            print("Invalid amount. Please enter a positive number.")
            
    except ValueError:
        print("Invalid input. Please enter a valid number.")
