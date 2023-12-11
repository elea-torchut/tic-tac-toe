import tkinter as tk
from tkinter import messagebox
from ia import ia

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [""] * 9  # Representing the game board
        self.current_player = "X"
        self.create_widgets()

    def create_widgets(self):
        self.buttons = [tk.Button(self.master, text="", font=('normal', 20), width=6, height=3,
                                  command=lambda i=i: self.on_button_click(i)) for i in range(9)]

        # Grid layout for buttons
        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            button.grid(row=row, column=col)

    def on_button_click(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, state=tk.DISABLED)

            print(f"Player {self.current_player} played at index {index}")
            print(f"Updated board: {self.board}")

            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_game()
            else:
                # Change de joueur seulement après que le joueur humain a joué
                self.master.after(1000, self.play_ai_turn)

    def play_ai_turn(self):
        self.current_player = "O"
    
        # Ajout de l'IA pour le joueur 'O'
        index_ia = ia(self.board, "O")  # Utiliser directement "O" comme le signe de l'IA
        if index_ia is not False:
            self.board[index_ia] = self.current_player
            self.buttons[index_ia].config(text=self.current_player, state=tk.DISABLED)

            print(f"AI played at index {index_ia}")
            print(f"Updated board: {self.board}")

            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_game()
            else:
                # Change de joueur après que l'IA a joué
                self.current_player = "X"

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != "":
                return True  # Vertical
            if self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != "":
                return True  # Horizontal

        if self.board[0] == self.board[4] == self.board[8] != "":
            return True  # Diagonal
        if self.board[2] == self.board[4] == self.board[6] != "":
            return True  # Diagonal

        return False

    def reset_game(self):
        for i in range(9):
            self.buttons[i].config(text="", state=tk.NORMAL)
            self.board[i] = ""
        self.current_player = "X"


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
