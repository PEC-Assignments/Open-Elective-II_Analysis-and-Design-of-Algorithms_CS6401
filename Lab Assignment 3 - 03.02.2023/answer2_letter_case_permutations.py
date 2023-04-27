# Solution Question 2 - Letter Case Permutation.

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


def letter_case_permutation(inp: str) -> list[str]:
    """a function to return all possible letter case permutations of a string.

    Args:
        inp (str): the string to be permuted

    Returns:
        list[str]: a list of all possible permutations
    """
    res = [""]
    for char in inp:
        if char.isalpha():
            res = [i + j for i in res for j in [char.upper(), char.lower()]]
        else:
            res = [i + char for i in res]
    return res


if __name__ == "__main__":
    print(*letter_case_permutation(input()))

# Complexity Analysis of the above solution:
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)

# Sample input:
# a1b2
