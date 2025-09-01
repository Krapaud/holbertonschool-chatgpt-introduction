def print_board(board):
    print("\n   0   1   2")
    for i, row in enumerate(board):
        print(f"{i}  " + " | ".join(row))
        if i < 2:
            print("  -----------")


def check_winner(board):
    # Vérifier les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]  # Retourner le joueur gagnant au lieu de True

    # Vérifier les colonnes
    for col in range(len(board[0])):
        if (board[0][col] == board[1][col] == board[2][col] and
                board[0][col] != " "):
            return board[0][col]  # Retourner le joueur gagnant

    # Vérifier la diagonale principale
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]  # Retourner le joueur gagnant

    # Vérifier la diagonale inverse
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]  # Retourner le joueur gagnant

    return None  # Pas de gagnant


def is_board_full(board):
    """
    Vérifie si le plateau est plein (match nul).

    Returns:
    bool: True si toutes les cases sont occupées, False sinon
    """
    for row in board:
        if " " in row:
            return False
    return True


def get_valid_input(prompt, valid_range):
    """
    Obtient une entrée valide de l'utilisateur avec validation complète.

    Parameters:
    prompt (str): Le message à afficher à l'utilisateur
    valid_range (tuple): Tuple (min, max) des valeurs acceptées

    Returns:
    int: Une valeur valide dans la plage spécifiée, ou None si annulé
    """
    while True:
        try:
            # Gestion d'erreur pour la conversion int
            user_input = input(prompt).strip()

            # Vérifier si l'entrée est vide
            if not user_input:
                print("Error: Please enter a value.")
                continue

            value = int(user_input)

            # Validation de la plage
            if value < valid_range[0] or value > valid_range[1]:
                print(f"Error: Please enter a number between "
                      f"{valid_range[0]} and {valid_range[1]}.")
                continue

            return value

        except ValueError:
            # Gestion d'erreur pour les entrées non-numériques
            print("Error: Invalid input. Please enter a number.")
            continue
        except KeyboardInterrupt:
            # Gestion de Ctrl+C
            print("\nGame cancelled.")
            return None


def tic_tac_toe():
    """
    Fonction principale du jeu tic-tac-toe avec validation complète des
    entrées. Gère tous les cas d'erreur possibles et détecte les matchs nuls.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    print("=== Welcome to Tic-Tac-Toe! ===")
    print("Players will take turns placing X and O.")
    print("Enter row and column numbers from 0 to 2.")

    try:
        while True:
            print_board(board)
            print(f"\nPlayer {player}'s turn")

            # Obtenir la ligne avec validation
            row = get_valid_input(f"Enter row (0, 1, or 2) for player "
                                  f"{player}: ", (0, 2))
            if row is None:  # L'utilisateur a annulé
                return

            # Obtenir la colonne avec validation
            col = get_valid_input(f"Enter column (0, 1, or 2) for player "
                                  f"{player}: ", (0, 2))
            if col is None:  # L'utilisateur a annulé
                return

            # Vérifier si la case est libre
            if board[row][col] == " ":
                board[row][col] = player

                # Vérifier s'il y a un gagnant
                winner = check_winner(board)
                if winner:
                    print_board(board)
                    print(f"\n🎉 Player {winner} wins! 🎉")
                    return

                # Vérifier le match nul
                if is_board_full(board):
                    print_board(board)
                    print("\n🤝 It's a tie! The board is full. 🤝")
                    return

                # Changer de joueur
                player = "O" if player == "X" else "X"

            else:
                print("❌ That spot is already taken! Try again.")

    except KeyboardInterrupt:
        # Gestion de Ctrl+C dans la boucle principale
        print("\n\nGame interrupted. Thanks for playing!")
    except Exception as e:
        # Gestion d'erreurs inattendues
        print(f"\nAn unexpected error occurred: {e}")
        print("Game terminated.")


# Correction : Protéger l'exécution du jeu
if __name__ == "__main__":
    tic_tac_toe()
