# Solution Question 1 - matrix search

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
except FileNotFoundError as e:
    pass


# ---------------------- Code Starts Here ----------------------#


def find_element(mat: list[list[int]], key: int) -> None:
    """a function to find the element in a matrix

    Args:
        mat (list[list[int]]): the matrix to be searched
        key (int): the element to be searched
    """

    # base case
    if not mat or len(mat) == 0:
        return

    # `M × N` matrix
    M, N = len(mat), len(mat[0])

    # start from `(0, N-1)`, i.e., top-rightmost cell of the matrix
    i = 0
    j = N - 1

    # run till matrix boundary is reached
    while i <= M - 1 and j >= 0:
        # if the current element is less than the key, increment row index
        if mat[i][j] < key:
            i = i + 1

        # if the current element is more than the key, decrement col index
        elif mat[i][j] > key:
            j = j - 1

        # if the current element is equal to the key
        else:
            print("Element", key, "is found at position", (i, j))
            i = i + 1
            j = j - 1


if __name__ == "__main__":
    R = int(input("Enter the number of rows: \n"))
    mtrx = [list(map(int, input(f"Enter the {i}th row: \n").split())) for i in range(R)]
    ele = int(input("Enter the element to be searched: \n"))
    # mtrx =
    #     -4, -3, -1, 3, 5
    #     -3, -2, 2, 4, 6
    #     -1, 1, 3, 5, 8
    #     3, 4, 7, 8, 9
    # ]

    find_element(mtrx, ele)

# Complexity Analysis of the above solution:
# Time Complexity - O(m+n)
# Space Complexity - O(1)
