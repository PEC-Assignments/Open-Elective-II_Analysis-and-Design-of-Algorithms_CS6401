# Solution Question 1 - Sort Stack

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

def sortedInsert(s, element):
    if len(s) == 0 or element > s[-1]:
        s.append(element)
        return
    else:
        temp = s.pop()
        sortedInsert(s, element)
        s.append(temp)


def sortStack(s):
    if len(s) != 0:
        temp = s.pop()
        sortStack(s)
        sortedInsert(s, temp)


if __name__ == "__main__":
    s = [30, -5, 18, 14, -3]
    sortStack(s)
    print(s)

# Complexity Analysis of the above solution:
# Time Complexity: O(n^2)
# Space Complexity: O(n)
