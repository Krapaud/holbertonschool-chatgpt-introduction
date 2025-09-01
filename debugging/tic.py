def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Vérifier les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérifier les colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérifier la diagonale principale
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    # Vérifier la diagonale secondaire
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    """Vérifier si le plateau est plein (égalité)"""
    for row in board:
        if " " in row:
            return False
    return True

def get_valid_input(prompt, valid_range):
    """Obtenir une entrée valide de l'utilisateur"""
    while True:
        try:
            value = int(input(prompt))
            if value in valid_range:
                return value
            else:
                print(f"Veuillez entrer un nombre entre {min(valid_range)} et {max(valid_range)}")
        except ValueError:
            print("Veuillez entrer un nombre valide")

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        print(f"\nTour du joueur {player}")
        
        # Obtenir des entrées valides avec gestion d'erreurs
        row = get_valid_input("Entrez la ligne (0, 1, ou 2): ", [0, 1, 2])
        col = get_valid_input("Entrez la colonne (0, 1, ou 2): ", [0, 1, 2])
        
        # Vérifier si la case est libre
        if board[row][col] == " ":
            board[row][col] = player
            
            # Vérifier s'il y a un gagnant
            if check_winner(board):
                print_board(board)
                print(f"Le joueur {player} a gagné !")
                break
            
            # Vérifier s'il y a égalité
            if is_board_full(board):
                print_board(board)
                print("Égalité ! Le plateau est plein.")
                break
            
            # Changer de joueur
            player = "O" if player == "X" else "X"
        else:
            print("Cette case est déjà occupée ! Essayez à nouveau.")

tic_tac_toe()