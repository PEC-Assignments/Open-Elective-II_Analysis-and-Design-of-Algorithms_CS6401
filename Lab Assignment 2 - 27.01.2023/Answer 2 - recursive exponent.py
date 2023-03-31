# Solution to Question 2 - Recursive Exponentiation.

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


def pow(i, e):
    if e == 1:
        return i
    else:
        return i * pow(i, e - 1)


if __name__ == "__main__":
    num, exp = map(int, input().strip().split())
    print(pow(num, exp))

# Complexity Analysis of the above solution:
# Time Complexity: O(n)
# Space Complexity: O(1)
