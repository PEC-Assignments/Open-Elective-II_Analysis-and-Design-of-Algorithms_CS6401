# Solution Question 2 - Strassen's Algorithm

# ---------------- MSB's Coding Template ---------------- #
"""
    "ɴᴏ ᴄᴏᴅᴇ ɪꜱ ᴘᴇʀꜰᴇᴄᴛ"
"""

# ---I/O from file---#
import sys
import numpy as np

try:
    sys.stdin = open("input.txt", "r", encoding="UTF-8")
    sys.stdout = open("output.txt", "w", encoding="UTF-8")
    sys.stderr = open("output.txt", "w", encoding="UTF-8")
except FileNotFoundError as __:
    pass


# ---------------------- Code Starts Here ----------------------#


def split(matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Split a given matrix into quarters.

    Args:
        matrix (np.ndarray): matrix to be split of shape n x n, where n is even

    Returns:
        tuple[np.ndarray]: tuple containing 4 n/2 x n/2 matrices corresponding to a,b,c,d
    """
    row, col = matrix.shape
    row2, col2 = row // 2, col // 2
    return (
        matrix[:row2, :col2],
        matrix[:row2, col2:],
        matrix[row2:, :col2],
        matrix[row2:, col2:],
    )


def strassen(x, y):
    """Calculates matrix product by divide and conquer approach of
    Strassen's Algorithm Matrix Multiplication Algorithm,recursively.

    Args:
        x (np.ndarray): first matrix of shape n x n, where n is even which is to be multiplied\n
        y (np.ndarray): Second matrix of shape n x n, where n is even which is to be multiplied

    Returns:
        np.ndarray: Product of x and y
    """

    # Base case when size of matrices is 1x1
    if len(x) == 1:
        return x * y

    # Splitting the matrices into quadrants. This will be done recursively
    # until the base case is reached.
    a, b, c, d = split(x)
    e, f, g, h = split(y)

    # Computing the 7 products, recursively (p1, p2...p7)
    p1 = strassen(a, f - h)
    p2 = strassen(a + b, h)
    p3 = strassen(c + d, e)
    p4 = strassen(d, g - e)
    p5 = strassen(a + d, e + h)
    p6 = strassen(b - d, g + h)
    p7 = strassen(a - c, e + f)

    # Computing the values of the 4 quadrants of the final matrix c
    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7

    # Combining the 4 quadrants into a single matrix by stacking horizontally and vertically.
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

    return c


if __name__ == "__main__":
    # Input matrices
    R = int(input("Enter the number of rows in the matrices: \n"))
    print("Enter the elements of the first matrix:")
    A = np.array([list(map(int, input().split())) for i in range(R)])
    input()
    print("Enter the elements of the second matrix:")
    B = np.array([list(map(int, input().split())) for i in range(R)])

    print(strassen(A, B))

# Complexity Analysis of the above solution:
# Time Complexity: O(n^2.81)
# Space Complexity: O(n^2)

# Sample Input:
# 4
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 2 2 2 2

# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 2 2 2 2
