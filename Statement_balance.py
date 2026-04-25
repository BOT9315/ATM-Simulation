def statement():
    import utils as np 
    
    total_deposit = sum(np.deposits)
    total_withdraw = sum(np.withdrawals)
    current_balance = total_deposit - total_withdraw
    print(f"\n--- Account Statement/History ---")
    print(f"Total Deposited in your account:  {total_deposit}")
    print(f"Total Withdrawn from your account:  {total_withdraw}")
    print(f"Current Balance in your account:  {current_balance}")
    print(f"-------------------------")
