import random
import time
import tkinter as tk

# Constants
WIDTH = 400  # Width of the grid in pixels
HEIGHT = 400  # Height of the grid in pixels
CELL_SIZE = 10  # Size of each cell in pixels
GRID_WIDTH = WIDTH // CELL_SIZE  # Number of cells in a row
GRID_HEIGHT = HEIGHT // CELL_SIZE  # Number of cells in a column
DELAY = 0.1  # Delay between generations in seconds

# Initialize the grid
grid = [[random.choice([0, 1]) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Initialize the GUI
root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

def update_grid():
    global grid
    
    # Create a new grid to hold the updated state of the cells
    new_grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            # Count the number of live neighbors
            live_neighbors = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    if 0 <= row + i < GRID_HEIGHT and 0 <= col + j < GRID_WIDTH:
                        live_neighbors += grid[row + i][col + j]
            
            # Apply the rules to update the state of the cell
            if grid[row][col] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[row][col] = 0
                else:
                    new_grid[row][col] = 1
            else:
                if live_neighbors == 3:
                    new_grid[row][col] = 1
                else:
                    new_grid[row][col] = 0
    
    grid = new_grid

def draw_grid():
    canvas.delete("all")
    
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            
            if grid[row][col] == 1:
                canvas.create_rectangle(x1, y1, x2, y2, fill="black")
    
    root.update()

def game_loop():
    while True:
        draw_grid()
        update_grid()
        time.sleep(DELAY)

# Start the game loop
game_loop()

# Start the Tkinter event loop
root.mainloop()
