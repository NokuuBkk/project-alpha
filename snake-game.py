# Snake Game with Tkinter (งูสีเขียว ใช้ลูกศรบังคับ)
import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title('Snake Game')
        self.canvas = tk.Canvas(root, width=400, height=400, bg='black')
        self.canvas.pack()
        self.snake = [(200, 200), (190, 200), (180, 200)]
        self.direction = 'Right'
        self.food = self.create_food()
        self.score = 0
        self.game_over = False
        self.root.bind('<Up>', lambda event: self.change_direction('Up'))
        self.root.bind('<Down>', lambda event: self.change_direction('Down'))
        self.root.bind('<Left>', lambda event: self.change_direction('Left'))
        self.root.bind('<Right>', lambda event: self.change_direction('Right'))
        self.score_label = tk.Label(root, text=f'Score: {self.score}', fg='white', bg='black')
        self.score_label.pack()
        self.update()

    def create_food(self):
        while True:
            x = random.randint(0, 39) * 10
            y = random.randint(0, 39) * 10
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, new_direction):
        opposite = {'Up': 'Down', 'Down': 'Up', 'Left': 'Right', 'Right': 'Left'}
        if new_direction != opposite.get(self.direction):
            self.direction = new_direction

    def move(self):
        if self.game_over:
            return
        head_x, head_y = self.snake[0]
        if self.direction == 'Up':
            head_y -= 10
        elif self.direction == 'Down':
            head_y += 10
        elif self.direction == 'Left':
            head_x -= 10
        elif self.direction == 'Right':
            head_x += 10
        new_head = (head_x, head_y)
        # Check collision
        if (
            head_x < 0 or head_x >= 400 or
            head_y < 0 or head_y >= 400 or
            new_head in self.snake
        ):
            self.game_over = True
            self.score_label.config(text='Game Over! Score: {}'.format(self.score))
            return
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.score_label.config(text=f'Score: {self.score}')
            self.food = self.create_food()
        else:
            self.snake.pop()

    def draw(self):
        self.canvas.delete('all')
        # Draw snake
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+10, y+10, fill='green', outline='')
        # Draw food
        fx, fy = self.food
        self.canvas.create_oval(fx, fy, fx+10, fy+10, fill='red', outline='')

    def update(self):
        self.move()
        self.draw()
        if not self.game_over:
            self.root.after(100, self.update)

if __name__ == '__main__':
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
