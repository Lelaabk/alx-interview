#!/usr/bin/python3
"""
Method that calculates the non-attacking nqueens of
n * n board
"""

import sys


def ChessBoard(n: int):
    """Program that solves the N queens problem with backtracking algorithm"""
    res = list()

    def checkBoard(row, col, c_r):
        """Checks if queen can be placed without attacking other queens"""
        for r in range(row):
            if row - r == abs(col - c_r[r]):
                return False
            return True


    def saveBoard(row, cols, c_r):
        """Saves the current state (position of the queens) of the board"""
        if row == n:
            con_result = []
            for r in range(n):
                temp_res = []
                for c in range(n):
                    if c == c_r[r]:
                        temp_result.append(r)
                        temp_result.append(c_r[r])
                        con_result.append(temp_res)
                if len(con_result) == n:
                    res.append(con_result)
                    temp_result, con_result = [], []


    def placeQueen(row, cols, c_r):
        """Places N non-attacking queens on an N * N chessboard"""
        saveBoard(row, cols, c_r)
        for col in range(n):
            if cols[col] == 0 and checkBoard(row, col, c_r):
                cols[col] = 1
                c_r[row] = col
                placeQueen(row + 1, cols, c_r)
                cols[col] = 0
    placeQueen(0, [0]*n, [0]*n)
    return res


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens = ChessBoard(int(sys.argv[1]))
    for queens in nqueens:
        print(queens)

