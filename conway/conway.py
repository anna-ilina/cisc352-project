import pyglet
import random
from copy import deepcopy
import fileinput
import sys

SLEEP = 1 / 10.0

WIDTH = 400
HEIGHT = 400

SIDE = 10

DENSITY = 0.5

window = pyglet.window.Window(WIDTH, HEIGHT)

def create_board(width, height):
    random.seed()
    board = []
    for y in range(0, height):
        row = []
        for x in range(0, width):
            if random.random() < DENSITY:
                row.append(True)
            else:
                row.append(False)
        board.append(row)
    return board

def update(dt):
    if dt < SLEEP:
        return
    update_board()

def update_board():
    global board
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            update_cell(x, y, cell)
    board = deepcopy(next_board)

def update_cell(x, y, alive):
    n = count_neighbours(x, y)
    if alive and (n == 2 or n == 3):
        next_board[y][x] = True
    elif not alive and n == 3:
        next_board[y][x] = True
    else:
        next_board[y][x] = False

OFFSETS = [[1, -1],
        [-1, 1],
        [1, 1],
        [-1, -1],
        [-1, 0],
        [0, -1],
        [1, 0],
        [0, 1]]

def count_neighbours(x, y):
    def within_bounds(coord):
        return coord[0] >= 0 and coord[0] < CHEIGHT and \
                coord[1] >= 0 and coord[1] < CWIDTH
    def is_living(coord):
        return board[coord[0]][coord[1]]
    def add_offset(coord):
        return [coord[0] + y, coord[1] + x]
    neighbours = list(map(add_offset, OFFSETS))
    neighbours = list(filter(within_bounds, neighbours))
    return len(list(filter(is_living, neighbours)))

@window.event
def on_draw():
    pyglet.gl.glColor4f(1, 1, 1, 1)
    draw_rectangle(0, 0, WIDTH, HEIGHT)
    pyglet.gl.glColor4f(0, 0, 0, 0)
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell:
                draw_cell(x, y)

def draw_cell(x, y):
    x1 = x * SIDE
    y1 = y * SIDE
    draw_rectangle(x1, y1, x1 + SIDE, y1 + SIDE)

def draw_rectangle(x1, y1, x2, y2):
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
            ('v2i', (x1, y1, x1, y2, x2, y2, x2, y1)))

def parse_board():
    def num_to_bool(num):
        num = int(num)
        if num == 1:
            return True
        else:
            return False
    b = []
    generations = 0
    first = True
    for line in fileinput.input():
        line = line.strip()
        if first:
            generations = int(line)
            first = False
            continue
        b.append(list(map(num_to_bool, list(line))))
    return b


if __name__ == '__main__':
    if len(sys.argv) > 1:
        board = parse_board()
        CHEIGHT= len(board)
        CWIDTH = len(board[0])
        next_board = deepcopy(board)
    else:
        CWIDTH = int(WIDTH / SIDE)
        CHEIGHT = int(HEIGHT / SIDE)
        board = create_board(CWIDTH, CHEIGHT)
        next_board = deepcopy(board)

    pyglet.clock.schedule_interval(update, SLEEP)
    pyglet.app.run()
