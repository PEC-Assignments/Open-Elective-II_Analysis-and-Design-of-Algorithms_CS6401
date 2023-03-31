# Solution to Question 1 - Check palindrome.

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


def check_palindrome(s):

    # General solution
    if len(s) == 0 or len(s) == 1:
        return "True"
    else:
        for i in range(len(s)//2):
            if s[i] != s[-i-1]:
                return "False"
        return "True"

    # Python specific solution
    '''
    return s == s[::-1]
    '''


if __name__ == "__main__":
    print(check_palindrome(input().strip().lower()))

# Complexity Analysis of the above solution:
# Time Complexity: O(n)
# Space Complexity: O(1)
