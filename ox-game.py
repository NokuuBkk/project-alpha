# OX Game (Tic-Tac-Toe) พื้นหลังสีดำ ด้วย Tkinter
import tkinter as tk

class OXGame:
    def __init__(self, root):
        self.root = root
        self.root.title('OX Game')
        self.canvas = tk.Canvas(root, width=300, height=300, bg='black')
        self.canvas.pack()
        self.board = ['' for _ in range(9)]
        self.current_player = 'X'
        self.buttons = []
        self.create_board()
        self.status_label = tk.Label(root, text='Player X', fg='white', bg='black', font=('Arial', 14))
        self.status_label.pack()

    def create_board(self):
        for i in range(9):
            btn = tk.Button(self.root, text='', font=('Arial', 24), width=4, height=2,
                            command=lambda idx=i: self.make_move(idx), bg='gray20', fg='white', activebackground='gray40')
            row, col = divmod(i, 3)
            btn.place(x=col*100+10, y=row*100+10, width=80, height=80)
            self.buttons.append(btn)

    def make_move(self, idx):
        if self.board[idx] == '' and not self.check_winner():
            self.board[idx] = self.current_player
            self.buttons[idx].config(text=self.current_player)
            winner = self.check_winner()
            if winner:
                self.status_label.config(text=f'Player {winner} wins!')
            elif '' not in self.board:
                self.status_label.config(text='Draw!')
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.status_label.config(text=f'Player {self.current_player}')

    def check_winner(self):
        wins = [
            [0,1,2], [3,4,5], [6,7,8], # rows
            [0,3,6], [1,4,7], [2,5,8], # cols
            [0,4,8], [2,4,6]           # diags
        ]
        for line in wins:
            a, b, c = line
            if self.board[a] == self.board[b] == self.board[c] != '':
                return self.board[a]
        return None

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('320x370')
    game = OXGame(root)
    root.mainloop()
