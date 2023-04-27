# Solution to Question 2 - Recursive Exponentiation.

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


def pwr(base: int, exp: int) -> int:
    """recursive function to calculate power of a number

    Args:
        base (int): base number\n
        exp (int): exponent

    Returns:
        int: result of base raised to the power of exp
    """

    if exp == 0:
        return 1

    temp = pwr(base, exp // 2)

    if exp % 2 == 0:
        return temp * temp
    return base * temp * temp


if __name__ == "__main__":
    num, ex = map(int, input().strip().split())
    print(pwr(num, ex))


# Complexity Analysis of the above solution:
# Time Complexity: O(n)
# Space Complexity: O(1)

# Sample input:
# 2 3
