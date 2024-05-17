import tkinter as tk
from tkinter import messagebox
import random

# Define the game constants
EMPTY, PLAYER1, PLAYER2, COMPUTER = " ", "X", "O", "O"

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.buttons = [tk.Button(self.root, text="", font=("normal", 25), width=8, height=4, command=lambda i=i: self.button_click(i)) for i in range(9)]
        for i, button in enumerate(self.buttons):
            button.grid(row=i // 3, column=i % 3)
        self.label = tk.Label(self.root, font=("normal", 16))
        self.label.grid(row=3, column=0, columnspan=3)
        self.start_button = tk.Button(self.root, text="Start Game", command=self.select_mode)
        self.start_button.grid(row=4, column=0, columnspan=3, pady=10)
        self.mode = None
        self.current_player = PLAYER1
        self.board = [EMPTY] * 9
        self.winner = None

    def select_mode(self):
        mode_dialog = tk.Toplevel(self.root)
        mode_dialog.title("Select Game Mode")

        mode_var = tk.StringVar()
        mode_var.set("1")  # Default to single player mode

        single_player_radio = tk.Radiobutton(mode_dialog, text="Single Player", variable=mode_var, value="1")
        two_player_radio = tk.Radiobutton(mode_dialog, text="Two Players", variable=mode_var, value="2")

        single_player_radio.pack(pady=5)
        two_player_radio.pack(pady=5)

        start_button = tk.Button(mode_dialog, text="Start Game", command=lambda: self.start_game(mode_var.get()))
        start_button.pack(pady=10)

        mode_dialog.mainloop()

    def start_game(self, mode):
        self.mode = int(mode)
        self.start_button.grid_forget()
        self.label.config(text="Player 1's turn (X)" if self.mode == 2 else "Your turn (X)")
        if self.mode == 1:
            self.computer_move()
        self.root.mainloop()

    def button_click(self, index):
        if self.board[index] == EMPTY and not self.winner:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            self.check_game_state()
            if self.mode == 2:
                self.current_player = PLAYER2 if self.current_player == PLAYER1 else PLAYER1
                self.label.config(text=f"Player {2 if self.current_player == PLAYER2 else 1}'s turn ({self.current_player})")
            else:
                self.computer_move()

    def computer_move(self):
        if self.board[4] == EMPTY:
            self.board[4] = COMPUTER
            self.buttons[4].config(text=COMPUTER)
        else:
            available_moves = [i for i in range(9) if self.board[i] == EMPTY]
            move = random.choice(available_moves) if available_moves else random.randint(0, 8)
            self.board[move] = COMPUTER
            self.buttons[move].config(text=COMPUTER)
        self.check_game_state()

    def check_winner(self, board):
        for fusion in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if board[fusion[0]] == board[fusion[1]] == board[fusion[2]] != EMPTY:
                for i in fusion:
                    self.buttons[i].config(bg="green")
                return board[fusion[0]]
        if EMPTY not in board:
            return "tie"
        return None

    def check_game_state(self):
        self.winner = self.check_winner(self.board)
        if self.winner == PLAYER1:
            messagebox.showinfo("Tic-Tac-Toe", "Player 1 wins!" if self.mode == 2 else "You win!")
            self.root.quit()
        elif self.winner == PLAYER2:
            messagebox.showinfo("Tic-Tac-Toe", "Player 2 wins!")
            self.root.quit()
        elif self.winner == COMPUTER:
            messagebox.showinfo("Tic-Tac-Toe", "Computer wins!")
            self.root.quit()
        elif self.winner == "tie":
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            self.root.quit()

if __name__ == "__main__":
    game = TicTacToe()
    game.select_mode()
