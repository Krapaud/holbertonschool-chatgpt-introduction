class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        # Validation ajoutée : vérifier que le montant est positif
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return False
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))
        return True

    def withdraw(self, amount):
        # Validation ajoutée : vérifier que le montant est positif
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
            return False
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))
            return True

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def get_valid_amount(prompt):
    """
    Fonction utilitaire pour obtenir un montant valide de l'utilisateur.
    Gère les erreurs de conversion et valide que le montant est positif.
    
    Parameters:
    prompt (str): Le message à afficher à l'utilisateur
    
    Returns:
    float: Un montant valide (positif) ou None si l'utilisateur annule
    """
    while True:
        try:
            # Gestion d'erreur pour la conversion float
            user_input = input(prompt).strip()
            
            # Vérifier si l'entrée est vide
            if not user_input:
                print("Error: Please enter a valid amount.")
                continue
                
            amount = float(user_input)
            
            # Validation : le montant doit être positif
            if amount <= 0:
                print("Error: Amount must be positive. Please try again.")
                continue
                
            return amount
            
        except ValueError:
            # Gestion d'erreur pour les entrées non-numériques
            print("Error: Invalid input. Please enter a numeric value.")
            continue
        except KeyboardInterrupt:
            # Gestion de Ctrl+C
            print("\nOperation cancelled.")
            return None

def main():
    cb = Checkbook()
    print("Welcome to your Checkbook!")
    
    while True:
        try:
            # Gestion d'erreur pour l'entrée de l'action
            action = input("\nWhat would you like to do? (deposit, withdraw, balance, exit): ").strip()
            
            if action.lower() == 'exit':
                print("Thank you for using your Checkbook. Goodbye!")
                break
            elif action.lower() == 'deposit':
                # Utilisation de la fonction de validation pour obtenir un montant sûr
                amount = get_valid_amount("Enter the amount to deposit: $")
                if amount is not None:  # Vérifier que l'utilisateur n'a pas annulé
                    cb.deposit(amount)
            elif action.lower() == 'withdraw':
                # Utilisation de la fonction de validation pour obtenir un montant sûr
                amount = get_valid_amount("Enter the amount to withdraw: $")
                if amount is not None:  # Vérifier que l'utilisateur n'a pas annulé
                    cb.withdraw(amount)
            elif action.lower() == 'balance':
                cb.get_balance()
            else:
                print("Invalid command. Please try again.")
                
        except KeyboardInterrupt:
            # Gestion de Ctrl+C dans le menu principal
            print("\n\nProgram interrupted. Goodbye!")
            break
        except EOFError:
            # Gestion de Ctrl+D (fin de fichier)
            print("\n\nEnd of input detected. Goodbye!")
            break

if __name__ == "__main__":
    main()