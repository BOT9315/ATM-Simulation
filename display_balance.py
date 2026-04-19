def display_balance():
    import utils as np
    current_balance = sum(np.deposits) - sum(np.withdrawals)
    if np.deposits or np.withdrawals:
        print(f"Current balance of your account: {current_balance}")
    else:
        print("No transactions yet. Balance is 0.")