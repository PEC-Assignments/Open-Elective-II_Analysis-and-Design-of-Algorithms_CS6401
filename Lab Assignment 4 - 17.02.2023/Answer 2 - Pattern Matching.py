# Question 2 Solution - Pattern Matching

# ---------------- MSB's Coding Template ---------------- #
'''
    "ɴᴏ ᴄᴏᴅᴇ ɪꜱ ᴘᴇʀꜰᴇᴄᴛ"
'''

# ---I/O from file---#
import sys
try:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    sys.stderr = open("output.txt", "w")
except:
    pass


# ---------------------- Code Starts Here ----------------------#

import re


def pattern_matching(text: str, pattern: str) -> bool:
    return bool(re.fullmatch(pattern, text))


if __name__ == "__main__":
    print(1 if pattern_matching(input(), input()) else 0)

# Analyzing the time complexity of the above code:
# Time Complexity: O(n)
# Space Complexity: O(n)
