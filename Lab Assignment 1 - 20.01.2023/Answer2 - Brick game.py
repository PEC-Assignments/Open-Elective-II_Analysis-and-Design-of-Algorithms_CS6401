# Solution of Question 2 -  Motu Patlu Brick Game.

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


def brick_game(n):
    rounds = int((((9+24*n)**0.5)-3)/6)
    bricks = (3*rounds + 3*(rounds**2))/2

    if n-bricks > rounds+1:
        return "Motu"
    elif n-bricks == 0:
        return "Motu"
    else:
        return "Patlu"


if __name__ == "__main__":
    print(brick_game(int(input())))

# Complexity Analysis of the above solution:
# Time Complexity: O(1)
# Space Complexity: O(1)
