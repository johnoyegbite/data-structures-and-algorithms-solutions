# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 21:15:29 2020

@author: johnoyegbite
"""
# SOLVED!

class Solution:
    def solveSudoku(self, board) -> None:
        """
        type board: : List[List[str]]
        Do not return anything, modify board in-place instead.
        """
        return self.solve_sudoku(board)
        # print(board)

    def solve_sudoku(self, board):
        row, col = self.findUnassigned(board)
        if row == -1 and col == -1:
            return True
        for num in "123456789":
            if self.isSafe(row, col, num, board):
                board[row][col] = num
                if self.solve_sudoku(board):
                    # board[row][col] = num
                    return True
                board[row][col] = "."
        return False

    def findUnassigned(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    return row, col
        return -1, -1

    def isSafe(self, row, col, val, board):
        if self.checkrow(row, val, board) and \
                self.checkcol(col, val, board) and \
                self.checksquare(row, col, val, board):
            return True
        return False

    def checkrow(self, row, val, board):
        for col in range(9):
            if board[row][col] == val:
                return False
        return True

    def checkcol(self, col, val, board):
        for row in range(9):
            if board[row][col] == val:
                return False
        return True

    def checksquare(self, row, col, val, board):
        boxrow = row - row % 3
        boxcol = col - col % 3
        for r in range(boxrow, boxrow+3):
            for c in range(boxcol, boxcol+3):
                if board[r][c] == val:
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    board = [
        [".", ".", ".", "7", ".", ".", "3", ".", "1"],
        ["3", ".", ".", "9", ".", ".", ".", ".", "."],
        [".", "4", ".", "3", "1", ".", "2", ".", "."],
        [".", "6", ".", "4", ".", ".", "5", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "1", ".", ".", "8", ".", "4", "."],
        [".", ".", "6", ".", "2", "1", ".", "5", "."],
        [".", ".", ".", ".", ".", "9", ".", ".", "8"],
        ["8", ".", "5", ".", ".", "4", ".", ".", "."]
    ]
    print(s.solveSudoku(board))
