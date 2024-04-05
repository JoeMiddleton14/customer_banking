"""Import the Account class from the Account.py file."""
from Account import Account

def create_cd_account(balance, interest_rate, months):
    # Create an instance of the Account class with initial balance and interest rate
    cd_account = Account(balance, interest_rate)

    # Calculate interest earned
    monthly_interest_rate = interest_rate / 12 / 100
    interest_earned = balance * (monthly_interest_rate * months)

    # Update balance by adding the interest earned
    updated_balance = balance + interest_earned
    cd_account.set_balance(updated_balance)

    # Set the interest earned using the set_interest method of the Account class
    cd_account.set_interest(interest_earned)

    return updated_balance, interest_earned

