import random

def check_winner(board, player):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True  # Vertical
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == player:
            return True  # Horizontal

    if board[0] == board[4] == board[8] == player:
        return True  # Diagonal
    if board[2] == board[4] == board[6] == player:
        return True  # Diagonal

    return False


def ia(board, signe):
    print("Inside the ia function")
    
    # Ajout d'impressions pour débogage
    print(f"Board received by ia: {board}")
    
    empty_indices = [i for i, val in enumerate(board) if val == ""]
    
    print(f"Empty indices: {empty_indices}")

    for index in empty_indices:
        temp_board = board.copy()
        temp_board[index] = "X" if signe == 'X' else "O"

        # Check if the AI can win in the next move
        if check_winner(temp_board, "X" if signe == 'X' else "O"):
            print(f"AI wants to play at index {index} to win.")
            return index

    for index in empty_indices:
        temp_board = board.copy()
        temp_board[index] = "X" if signe == 'O' else "O"

        # Check if the player can win in the next move and block them
        if check_winner(temp_board, "X" if signe == 'O' else "O"):
            print(f"AI wants to play at index {index} to block the player.")
            return index

    # If no winning move, choose a random empty spot
    if empty_indices:
        random_index = random.choice(empty_indices)
        print(f"AI chose a random index {random_index}.")
        return random_index

    print("AI couldn't decide where to play.")
    return False

