# Solution to Question 1 - Check palindrome.

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


def check_palindrome(inp: str) -> str:
    """A function to check if a string is a palindrome or not.

    Args:
        inp (str): string to be checked

    Returns:
        str: the string "True" if the string is a palindrome else "False"
    """

    # Python specific solution
    # return inp == inp[::-1]

    # General solution
    if len(inp) == 0 or len(inp) == 1:
        return "True"
    for i in range(len(inp) // 2):
        if inp[i] != inp[-i - 1]:
            return "False"
    return "True"


if __name__ == "__main__":
    print(check_palindrome(input().strip().lower()))

# Complexity Analysis of the above solution:
# Time Complexity: O(n)
# Space Complexity: O(1)
