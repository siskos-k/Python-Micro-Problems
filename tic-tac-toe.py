import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("300x300")
        self.player_turn = "X"
        self.board = [None] * 9
        self.buttons = []

        for i in range(9):
            button = tk.Button(self.window, text="", command=lambda i=i: self.click(i), height=3, width=6)
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def click(self, i):
        if self.board[i] is None:
            self.board[i] = self.player_turn
            self.buttons[i].config(text=self.player_turn)
            self.player_turn = "O" if self.player_turn == "X" else "X"
            self.check_winner()

    def check_winner(self):
        for i in range(3):
            if self.board[i*3] == self.board[i*3+1] == self.board[i*3+2] != None:
                self.game_over(self.board[i*3])
                return
            if self.board[i] == self.board[i+3] == self.board[i+6] != None:
                self.game_over(self.board[i])
                return
        if self.board[0] == self.board[4] == self.board[8] != None:
            self.game_over(self.board[0])
            return
        if self.board[2] == self.board[4] == self.board[6] != None:
            self.game_over(self.board[2])
            return
        if all(i is not None for i in self.board):
            self.game_over("Tie")

    def game_over(self, winner):
        message = "Game Over! " + winner + " wins!" if winner != "Tie" else "Game Over! It's a tie!"
        messagebox.showinfo("Tic Tac Toe", message)
        self.window.quit()

if __name__ == "__main__":
    game = TicTacToe()
    tk.mainloop()
