# Solution to Question : Sudoku Solver

# ---------------- MSB's Coding Template ---------------- #
"""
    "ɴᴏ ᴄᴏᴅᴇ ɪꜱ ᴘᴇʀꜰᴇᴄᴛ"
"""

# ---I/O from file---#
import sys

try:
    sys.stdin = open("input.txt", "r", encoding="UTF-8")
    sys.stdout = open("output.txt", "w", encoding="UTF-8")
    sys.stderr = open("output.txt", "w", encoding="UTF-8")
except FileNotFoundError as __:
    pass


# ---------------------- Code Starts Here ----------------------#
class Solution:
    """Sudoku Solver"""

    def __init__(self):
        self.size = 9
        self.sudoku_values = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        self.empty = "."
        self.row_no = lambda cell_no: cell_no // self.size  # Get row from cell. no
        self.col_no = lambda cell_no: cell_no % self.size  # Get col from cell. no
        self.box_no = lambda r, c: 3 * (r // 3) + c // 3  # Get box from row and column
        self.rows_values = {}  # {row: sudoku values set}
        self.cols_values = {}  # {col: sudoku values set}
        self.boxes_values = {}  # {box: sudoku values set}

    def solveSudoku(self, board: list[list[str]]) -> None:
        """Solves the sudoku board in-place

        Args:
            board (list[list[str]]): sudoku board
        """
        # 1. Initialization: Store all board values
        for i in range(self.size):
            self.rows_values[i] = set()
            self.cols_values[i] = set()
            self.boxes_values[i] = set()

        for r in range(self.size):
            for c in range(self.size):
                if board[r][c] != self.empty:
                    self.rows_values[r].add(board[r][c])
                    self.cols_values[c].add(board[r][c])
                    self.boxes_values[self.box_no(r, c)].add(board[r][c])

        # 2. Backtrack from cell no: 0
        self.backtrack(0, board)

    def backtrack(self, cell_no: int, board: list[list[str]]) -> bool:
        """Backtracking algorithm to solve sudoku

        Args:
            cell_no (int): the cell no. to start from\n
            board (list[list[str]]): sudoku board

        Returns:
            bool: True if solved else False
        """
        # Base case: we filled all empty cells
        if cell_no == 81:
            return True

        r, c = self.row_no(cell_no), self.col_no(cell_no)

        if board[r][c] != self.empty:
            return self.backtrack(cell_no + 1, board)

        for val in self.sudoku_values:
            # could_place? Is valid?
            if (
                val in self.rows_values[r]
                or val in self.cols_values[c]
                or val in self.boxes_values[self.box_no(r, c)]
            ):
                continue

            # place:
            board[r][c] = val
            self.rows_values[r].add(val)
            self.cols_values[c].add(val)
            self.boxes_values[self.box_no(r, c)].add(val)

            # next:
            if self.backtrack(cell_no + 1, board):
                return True

            # remove:
            board[r][c] = self.empty
            self.rows_values[r].remove(val)
            self.cols_values[c].remove(val)
            self.boxes_values[self.box_no(r, c)].remove(val)

        return False

    def printing(self, arr: list[list[str]]):
        """Prints the sudoku board

        Args:
            arr (list[list[str]]): sudoku board
        """
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end=" ")
            print()


if __name__ == "__main__":
    brd = [list(input().split()) for _ in range(9)]
    ob = Solution()
    ob.solveSudoku(brd)
    ob.printing(brd)

# Complexity Analysis of the above approach:
# Time Complexity: O(9^(n*n)).
# Space Complexity: O(n*n).

# Sample Input:
# 5 3 . . 7 . . . .
# 6 . . 1 9 5 . . .
# . 9 8 . . . . 6 .
# 8 . . . 6 . . . 3
# 4 . . 8 . 3 . . 1
# 7 . . . 2 . . . 6
# . 6 . . . . 2 8 .
# . . . 4 1 9 . . 5
# . . . . 8 . . 7 9
