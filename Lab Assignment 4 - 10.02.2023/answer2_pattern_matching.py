# Question 2 Solution - Pattern Matching

# ---------------- MSB's Coding Template ---------------- #
"""
    "ɴᴏ ᴄᴏᴅᴇ ɪꜱ ᴘᴇʀꜰᴇᴄᴛ"
"""

import re

# ---I/O from file---#
import sys

try:
    sys.stdin = open("input.txt", "r", encoding="UTF-8")
    sys.stdout = open("output.txt", "w", encoding="UTF-8")
    sys.stderr = open("output.txt", "w", encoding="UTF-8")
except FileNotFoundError as e:
    pass


# ---------------------- Code Starts Here ----------------------#


def pattern_matching(text: str, pattern: str) -> bool:
    """a function to check if a string matches a given pattern.

    Args:
        text (str): the string to be checked
        pattern (str): the pattern to be matched

    Returns:
        bool: returns True if the string matches the pattern else False
    """
    return bool(re.fullmatch(pattern, text))


if __name__ == "__main__":
    print(1 if pattern_matching(input(), input()) else 0)

# Complexity analysis of the above solution:
# Time Complexity: O(n)
# Space Complexity: O(n)
