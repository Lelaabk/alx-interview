#!/usr/bin/python3
"""
Method to solve the N Queens problem on an N x N chessboard
using backtracking.
"""
import sys


def solve_n_queens(board_size):
    """Solves the N Queens problem using backtracking."""

    def is_position_valid(pos, occupied_pos):
        """Checks if placing a queen at the given column position is valid."""
        for i in range(len(occupied_pos)):
            if (
                occupied_pos[i] == pos or
                occupied_pos[i] - i == pos - len(occupied_pos) or
                occupied_pos[i] + i == pos + len(occupied_pos)
            ):
                return False
        return True

    def place_queens_on_board(board_size, index, occupied_pos, solutions):
        """Recursively places queens on the board and records valid solutions."""
        if index == board_size:
            solutions.append(occupied_pos[:])
            return

        for i in range(board_size):
            if is_position_valid(i, occupied_pos):
                occupied_pos.append(i)
                place_queens_on_board(board_size, index + 1, occupied_pos, solutions)
                occupied_pos.pop()

    solutions = []
    place_queens_on_board(board_size, 0, [], solutions)
    return solutions


def main():
    """Main function to handle user input and output solutions."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(board_size)
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])


if __name__ == "__main__":
    main()