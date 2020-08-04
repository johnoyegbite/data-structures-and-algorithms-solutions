# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 17:01:34 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    According to the Wikipedia's article: "The Game of Life, 
    also known simply as Life, is a cellular automaton devised by the British 
    mathematician John Horton Conway in 1970."

    Given a board with m by n cells, each cell has an initial state live (1) 
    or dead (0). Each cell interacts with its eight neighbors (horizontal, 
    vertical, diagonal) using the following four rules (taken from the above 
    Wikipedia article):

    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    
    Write a function to compute the next state (after one update) of the board
    given its current state. The next state is created by applying the above 
    rules simultaneously to every cell in the current state, where births and 
    deaths occur simultaneously.

Example :
    Input: 
        [
            [0,1,0],
            [0,0,1],
            [1,1,1],
            [0,0,0]
        ]
    Output: 
        [
            [0,0,0],
            [1,0,1],
            [0,1,1],
            [0,1,0]
        ]

Challenge:
    Could you solve it in-place? Remember that the board needs to be updated 
    at the same time: You cannot update some cells first and then use their 
    updated values to update other cells.
    
    In this question, we represent the board using a 2D array. In principle, 
    the board is infinite, which would cause problems when the active area 
    encroaches the border of the array. How would you address these problems?
"""
import numpy as np


def get_live_neighbours(x, y, row_count, col_count, prev_state):
    live_neighbours = 0
    print(f"{x, y}")
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            x_n, y_n = x + i, y + j
            if 0 <= x_n < row_count and 0 <= y_n < col_count:
                if prev_state[x_n][y_n] == 1:
                    live_neighbours += 1
    return live_neighbours


def gameOfLife(board):
    """
    type board: the given board
    rtype: nothing
    """
    # Write your code here
    
    row_count = len(board)
    col_count = len(board[0])
    
    # prev_state = board.copy() # This is wrong it would still mutate the values in prev_state
    prev_state = ([[board[r][c] for c in range(col_count)] for r in range(row_count)])
    
    for x in range(row_count):
        for y in range(col_count):
            live_neighbours = get_live_neighbours(x, y, row_count, col_count, prev_state)
            if prev_state[x][y] == 0:
                if live_neighbours == 3: # state 4
                    board[x][y] = 1
            else:
                if live_neighbours < 2: # state 1: change to 0
                    board[x][y] = 0
                elif live_neighbours < 4: # state 2: change to 1
                    board[x][y] = 1
                else:                     # state 3: change to 0
                    board[x][y] = 0
    
                
if __name__ == "__main__":
    board = np.array([
                [0,1,0],
                [0,0,1],
                [1,1,1],
                [0,0,0]
                ])
    # End state
    # [
    #  [0,0,0],
    #  [1,0,1],
    #  [0,1,1],
    #  [0,1,0]
    # ]
    print(gameOfLife(board))
    print(board)
    