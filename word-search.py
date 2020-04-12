# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 21:32:14 2019

@author: USER
"""
# SOLVED!
"""
Problem: Given a 2D board and a word, find if the word exists in the grid.

         The word can be constructed from letters of sequentially adjacent cell, 
         where "adjacent" cells are those horizontally or vertically neighboring. 
         The same letter cell may not be used more than once.
         
Example:
    board =
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
def DFS(coord, board, visited, word_seen, word):
    x, y = coord
    visited[coord] = True
    word_seen.append(board[x][y])
    
    if word_seen == word:
        return True
    
    len_word_seen = len(word_seen)
    if word_seen != word[:len_word_seen]:
        word_seen.pop()
        del visited[(x, y)]
        return False
    
    # The nested for loops traverse through all the neigbouring vertical and
    # horizontal coordinates (these are the valid neighbouring coord for this problem). 
    # "LINE  **" TO "LINE ***" gets all the valid neighbouring coord
    row_max, col_max = len(board), len(board[0])
    for i in range(-1, 2): # ------ LINE **
        for j in range(-1, 2):
            # only look at the vertical and horizontal coordinates and not diagonal
            # if we see any diagonal coordinates, we continue
            if (i == j) or (i == -j): # -1, -1 | 0, 0 | -1, 1 | 1, -1 | 1, 1
                continue
            # This is either the vertical or horizontal neighbouring coord
            x_n, y_n = x + i, y + j 
            # Check if coord is valid before recursing
            if (0 <= x_n < row_max) and (0 <= y_n < col_max): # ------ LINE ***
                new_coord = (x_n, y_n)
                if new_coord not in visited:
                    seen = DFS(new_coord, board, visited, word_seen, word)
                    if seen:
                        return seen
                
    word_seen.pop()
    del visited[coord]
    return False

def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    row_count = len(board)
    col_count = len(board[0])
    board_coord = [(r, c) for r in range(row_count) for c in range(col_count)]
    
    seen = False
    for coord in board_coord:
        x, y = coord
        # check if this coordinates value is the first character of 'word'
        if board[x][y] == word[0]:
            visited = {}
            word_seen = []
            seen = DFS(coord, board, visited, word_seen, list(word))
            if seen:
                return seen
    return seen


if __name__ == "__main__":                
    board = [
                ['A','B','C','E'],
                ['S','F','C','S'],
                ['A','D','E','E']
                ]
    word = "SEE" # True
    word = "ABCCED" # True
    word = "ABCD" # False
    
    board = [
              ["a","b"],
              ["c","d"]
              ]
    word = "abcd" # False
    word = "acdb" # True
    
    board = [
                ["A","B","C","E"],
                ["S","F","E","S"],
                ["A","D","E","E"]
                ]
    word = "ABCESEEEFS"
    # word = "SEE"

    print(exist(board, word))