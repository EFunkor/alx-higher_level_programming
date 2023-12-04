#!/usr/bin/python3

"""
importing the sys module
"""

import sys
"""
Definition of an is_safe method.

"""


def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True


"""
solving the queens problem.
"""


def solve_nqueens(n):
    solutions = []
    if n < 4:
        return solutions

    def solve(board, col):
        if col == n:
            solutions.append(board[:])
            return
        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                solve(board, col + 1)
                board[i][col] = 0

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve(board, 0)
    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        positions = []
        for i in range(len(solution)):
            for j in range(len(solution[i])):
                if solution[i][j] == 1:
                    positions.append([i, j])
        print(positions)
