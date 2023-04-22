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


def strassen_algorithm(x: list[list[int]], y: list[list[int]]) -> list[list[int]]:
    """a function to multiply two matrices using Strassen's Algorithm

    Args:
        x (list[list[int]]): the first matrix to be multiplied
        y (list[list[int]]): the second matrix to be multiplied

    Returns:
        list[list[int]]: the product of the two matrices
    """
    if x.size == 1 or y.size == 1:
        return x * y

    n = x.shape[0]

    if n % 2 == 1:
        x = np.pad(x, (0, 1), mode="constant")
        y = np.pad(y, (0, 1), mode="constant")

    m = int(np.ceil(n / 2))
    a = x[:m, :m]
    b = x[:m, m:]
    c = x[m:, :m]
    d = x[m:, m:]
    e = y[:m, :m]
    f = y[:m, m:]
    g = y[m:, :m]
    h = y[m:, m:]
    p1 = strassen_algorithm(a, f - h)
    p2 = strassen_algorithm(a + b, h)
    p3 = strassen_algorithm(c + d, e)
    p4 = strassen_algorithm(d, g - e)
    p5 = strassen_algorithm(a + d, e + h)
    p6 = strassen_algorithm(b - d, g + h)
    p7 = strassen_algorithm(a - c, e + f)
    result = np.zeros((2 * m, 2 * m), dtype=np.int32)
    result[:m, :m] = p5 + p4 - p2 + p6
    result[:m, m:] = p1 + p2
    result[m:, :m] = p3 + p4
    result[m:, m:] = p1 + p5 - p3 - p7

    return result[:n, :n]


if __name__ == "__main__":
    A = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    B = np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])
    print("Matrix multiplication result: ")
    print(strassen_algorithm(A, B))


# Complexity Analysis of the above solution:
# Time Complexity: O(n^2.8074)
# Space Complexity: O(log(n))
