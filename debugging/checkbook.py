#!/usr/bin/python3
"""
Checkbook management system with deposit, withdrawal, and balance operations.
"""


class Checkbook:
    """A simple checkbook management system."""

    def __init__(self):
        """Initialize a new checkbook with zero balance."""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit money into the checkbook.

        Args:
            amount (float): The amount to deposit.

        Returns:
            bool: True if deposit successful, False otherwise.
        """
        # Validation: check that the amount is positive
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return False
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")
        return True

    def withdraw(self, amount):
        """
        Withdraw money from the checkbook.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if withdrawal successful, False otherwise.
        """
        # Validation: check that the amount is positive
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
            return False
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")
        return True

    def get_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.balance:.2f}")


def get_valid_amount(prompt):
    """
    Utility function to get a valid amount from the user.
    Handles conversion errors and validates that the amount is positive.

    Parameters:
    prompt (str): The message to display to the user

    Returns:
    float: A valid (positive) amount or None if the user cancels
    """
    while True:
        try:
            # Handle error for float conversion
            user_input = input(prompt).strip()

            # Check if the input is empty
            if not user_input:
                print("Error: Please enter a valid amount.")
                continue

            amount = float(user_input)

            # Validation: the amount must be positive
            if amount <= 0:
                print("Error: Amount must be positive. Please try again.")
                continue

            return amount

        except ValueError:
            # Handle error for non-numeric inputs
            print("Error: Invalid input. Please enter a numeric value.")
            continue
        except KeyboardInterrupt:
            # Handle Ctrl+C
            print("\nOperation cancelled.")
            return None


def main():
    """Main function to run the checkbook application."""
    cb = Checkbook()
    print("Welcome to your Checkbook!")

    while True:
        try:
            # Handle input action error
            prompt = "\nWhat would you like to do? " \
                    "(deposit, withdraw, balance, exit): "
            action = input(prompt).strip()

            if action.lower() == 'exit':
                print("Thank you for using your Checkbook. Goodbye!")
                break
            if action.lower() == 'deposit':
                # Use validation function to get a safe amount
                amount = get_valid_amount("Enter the amount to deposit: $")
                if amount is not None:  # Check that the user
                    # did not cancel
                    cb.deposit(amount)
            elif action.lower() == 'withdraw':
                # Use validation function to get a safe amount
                amount = get_valid_amount("Enter the amount to withdraw: $")
                if amount is not None:  # Check that the user
                    # did not cancel
                    cb.withdraw(amount)
            elif action.lower() == 'balance':
                cb.get_balance()
            else:
                print("Invalid command. Please try again.")

        except KeyboardInterrupt:
            # Handle Ctrl+C in the main menu
            print("\n\nProgram interrupted. Goodbye!")
            break
        except EOFError:
            # Handle Ctrl+D (end of file)
            print("\n\nEnd of input detected. Goodbye!")
            break


if __name__ == "__main__":
    main()
