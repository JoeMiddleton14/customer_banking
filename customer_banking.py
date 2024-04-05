from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    savings_balance = float(input("What is your initial savings account balance? "))
    savings_interest_rate = float(input("What is your APR for your savings account? "))
    savings_months = int(input("What is the length of months for savings account? "))
    
    savings_updated_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest_rate, savings_months)

    print(f"Savings Account:")
    print(f"Interest earned: ${savings_interest_earned}")
    print(f"Updated balance after {savings_months} months: ${savings_updated_balance}")

    cd_balance = float(input("Enter the CD account balance: "))
    cd_interest_rate = float(input("Enter the APR interest rate for the CD account: "))
    cd_months = int(input("Enter the number of months for the CD account: "))

    cd_updated_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    print(f"\nCD Account:")
    print(f"Interest earned: ${cd_interest_earned}")
    print(f"Updated balance after {cd_months} months: ${cd_updated_balance}")

    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """

    cd_balance = float(input("What is your initial CD balance? "))
    interest_rate = float(input("What is your APR? "))
    cd_months = int(input("What is the length of months for savings account? "))

    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("What is your initial savings account balance? "))
    savings_interest_rate = float(input("What is your APR for your savings account? "))
    savings_months = int(input("What is the length of months for savings account? "))


    # Call the create_savings_account function and pass the variables from the user.
    create_savings_account = create_savings_account(savings_balance, savings_interest_rate, savings_months)

if __name__ == "__main__":
    # Call the main function.
    main()

