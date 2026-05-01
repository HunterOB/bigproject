""""""

import time
import queue
import random

def print_grid():
    for row in grid:
        print(row)

def start_end():
    start, end = 0, 0
    while start == end:
        start = [random.randint(0, 19), random.randint(0, 19)]
        end = [random.randint(0, 19), random.randint(0, 19)]
        
    grid[start[0]][start[1]] = 1
    grid[end[0]][end[1]] = 2
    return grid, start, end


def distance(a, b):
    return round(((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5, 4)

def open_list_update(closed_list, start_node, open_list):
    allowerd_squares = [0, 1, 2]
    squares = [(1,1), (1,0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]
    for square in squares:
        new_x = square[0] + start_node[0]
        new_y = square[1] + start_node[1]
        if new_x > -1 and new_x < 20 and new_y > -1 and new_y < 20:
            if grid[new_y][new_x] in allowerd_squares and (new_x, new_y) not in closed_list:
                open_list.append((new_x, new_y))

    return open_list

def f_value(start, current_node, end):
    g = distance(start, current_node)
    h = distance(current_node, end)
    f = g + h
    return (g, h, f)
    

def a_star(start, end):
    open_list = []
    closed_list = [tuple(start)]

    open_list.append(start)
    
    while len(open_list) > 0:
        open_list = open_list_update(closed_list, closed_list[0], open_list)
        values = []
        for i in open_list:
            values.append(f_value(start, i, end))
        index = 0
        for i in range(1, len(values)):
            if values[index][2] > values[i][2]:
                index = i
        closed_list.append(open_list[i])

        print(closed_list)
        print(end)
        time.sleep(0.3)
        
        if closed_list[-1] == end:
            return closed_list

    
    
    

grid = [[0 for x in range(20)] for i in range(20)]
grid, start, end = start_end()
closed_list = a_star(start, tuple(end))